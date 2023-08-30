import uuid
from xapi_app.actions import cmi5
from xapi_app.types import XAPIStatement, XAPIActor, XAPIObject, XAPIContext, XAPIState
from xapi_app.actions.template import factory


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
        task_queue.append(cmi5.Launched(actor, lecture_object, lecture_context)), 
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

    def _run(self, task_queue: list):
        total_score = {
            "max": 0,
            "min": 0,
            "scaled": 0,
            "raw": 0,
        }

        while task_queue:
            # TODO: cmi5와 contents의 run을 분리할 것 
            task_instance = task_queue.pop()
            score = task_instance.start(
                attempt=self.attempt,
                session_id=self.session_id,
                total_score=total_score
            )

            if score:
                total_score["max"] = score["max"]
                total_score["raw"] = score["raw"]
                total_score["scaled"] = score["raw"] / score["max"]
            
            yield self._result_model(
                task_instance, 
                task_instance.actor, 
                task_instance.obj, 
                task_instance.verb, 
                task_instance.result, 
                task_instance.context
            )

    def _result_model(self, task_instance, actor, obj, verb, result, context):
        state = None
        stmt = XAPIStatement(
            actor=actor,
            object=obj,
            verb=verb,
            result=result,
            context=context
        )
        
        if task_instance.has_state():
            state = XAPIState(**task_instance.to_state())

        return stmt.to_full_statement(), state