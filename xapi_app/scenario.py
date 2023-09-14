import uuid
from copy import deepcopy
import random
from xapi_app.actions import cmi5
from xapi_app.actions.contents.actions import peer
from xapi_app.types import XAPIStatement, XAPIActor, XAPIObject, XAPIContext, XAPIState
from xapi_app.actions.template import factory
from copy import deepcopy


class Cmi5Scenario: 
    def __init__ (
        self, 
        attempt,
        session_id,
        actor: dict, 
        lecture_object_context: dict,
        contents_object_context: list[dict] = None,
    ):
        self.actor = actor
        self.attempt = attempt
        self.lecture = lecture_object_context
        self.contents = contents_object_context
        self.session_id = session_id

    def run_complted_with_contents(self):
        actor = XAPIActor(**self.actor)

        lecture_object = XAPIObject(**self.lecture["object"])
        lecture_context = XAPIContext(**self.lecture["context"])

        task_queue = []
        task_queue.append(cmi5.Launched(actor, lecture_object, lecture_context))
        task_queue.append(cmi5.Initialized(actor, lecture_object, lecture_context)) 

        for contents in self.contents:
            keys =[] 
            
            definition = contents["object"]["definition"]
            keys.append(definition['extensions']["https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/type"])
            
            if "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/content-type" in definition['extensions']:
                keys.append(definition['extensions']["https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/content-type"])
            
            if "interactionType" in definition:
                keys.append(definition["interactionType"])

            template = factory.get_template(*keys)()
            contents_obj = XAPIObject(**contents["object"])
            contents_context = XAPIContext(**contents["context"])
            for task_class in template.actions():
                task_queue.append(task_class(actor, contents_obj, contents_context))

        task_queue.append(cmi5.Completed(actor, lecture_object, lecture_context))
        return self._run(task_queue)
    
    def run_peer_submit(self, subimit_id):
        actor = XAPIActor(**self.actor)
        lecture_object = XAPIObject(**self.lecture["object"])
        lecture_context = XAPIContext(**self.lecture["context"])

        task_queue = []
        task_queue.append(cmi5.Launched(actor, lecture_object, lecture_context)), 
        task_queue.append(cmi5.Initialized(actor, lecture_object, lecture_context))
    
        for contents in self.contents:
            copy_contents = deepcopy(contents)
            copy_contents = self._regenerate_contents_id(copy_contents, subimit_id)

            keys = ["peer", "submit"] 
            template = factory.get_template(*keys)()
            contents_obj = XAPIObject(**copy_contents["object"])
            contents_context = XAPIContext(**copy_contents["context"])
            for task_class in template.actions():
                task_queue.append(task_class(actor, contents_obj, contents_context))

        task_queue.append(cmi5.Completed(actor, lecture_object, lecture_context))
        return self._run(task_queue)

    def run_peer_review(self, reviewer, submit_id, contents_id, assessment_type=None):
        actor = XAPIActor(**reviewer)
        lecture_object = XAPIObject(**self.lecture["object"])
        lecture_context = XAPIContext(**self.lecture["context"])

        task_queue = []
        task_queue.append(cmi5.Launched(actor, lecture_object, lecture_context)), 
        task_queue.append(cmi5.Initialized(actor, lecture_object, lecture_context))
    
        for contents in self.contents:
            copy_contents = deepcopy(contents)
            copy_contents = self._regenerate_contents_id(copy_contents, contents_id)
            copy_contents["object"]["definition"]["extensions"]["https://class.whalespace.io/chapters/chapter/lectures/lecture/assessment-type"] = assessment_type
            keys = ["peer", "review"] 
            template = factory.get_template(*keys)()
            contents_obj = XAPIObject(**copy_contents["object"])
            contents_context = XAPIContext(**copy_contents["context"])
            for task_class in template.actions():
                task_queue.append(task_class(actor, contents_obj, contents_context))

        task_queue.append(cmi5.Completed(actor, lecture_object, lecture_context))
        return self._run(task_queue, submit_id)
    
    def run_peer_scored(self, subimit_id):
        actor = XAPIActor(**self.actor)
        task_queue = []
        for contents in self.contents: 
            copy_contents = deepcopy(contents)
            copy_contents = self._regenerate_contents_id(copy_contents, subimit_id)   
            contents_obj = XAPIObject(**copy_contents["object"])
            contents_context = XAPIContext(**copy_contents["context"])
            task_queue.append(peer.ReviewScored(actor, contents_obj, contents_context))
        return self._run(task_queue)

    def _run(self, task_queue: list, submit_id=None):
        total_score = {
            "max": 0,
            "min": 0,
            "scaled": 0,
            "raw": 0,
        }
        content_id = submit_id
        while task_queue:
            # TODO: cmi5와 contents의 run을 분리할 것 
            task_instance = task_queue.pop(0)
            score = task_instance.start(
                attempt=self.attempt,
                session_id=self.session_id,
                total_score=total_score,
                content_id=content_id
            )
            
            yield self._result_model(task_instance)

    def _result_model(self, task_instance):
        state = None
        stmt = XAPIStatement(
            actor=task_instance.actor,
            object=task_instance.obj,
            verb=task_instance.verb,
            result=task_instance.result,
            context=task_instance.context
        )
        
        if task_instance.has_state():
            state = XAPIState(*task_instance.to_state())

        return stmt.to_full_statement(), state
    

    def _regenerate_contents_id(self, contents_object_context, contents_id):
        contents_object_context['object']['definition']['extensions']['https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/content-id'] = contents_id
        contents_object_context['object']['id'] = contents_object_context['object']['id'][:contents_object_context['object']['id'].rindex("/")] + "/" + str(contents_id)
        return contents_object_context