import uuid
from xapi_app.actions import cmi5
from xapi_app.types import XAPIStatement, XAPIActor, XAPIObject, XAPIContext, XAPIState
from xapi_app.actions.template import ContentsFactory, factory


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
        tasks = [
            cmi5.Launched, 
            cmi5.Initialized, 
            ContentsFactory,
            cmi5.Completed,
        ]
        
        return self._run(tasks)

    def _is_trigger_contents(self, task):
        return issubclass(ContentsFactory, task)

    def _run(self, tasks):
        actor = XAPIActor(**self.actor)
        lecture_object = XAPIObject(**self.lecture["object"])
        lecture_context = XAPIContext(**self.lecture["context"])
        
        for task in tasks:
            # Contents일 경우
            if self._is_trigger_contents(task):
                for contents in self.contents:
                    definition = contents["object"]["definition"]
                    keys = []
                    keys.append(definition['extensions']["https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/type"])
                    if "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/content-type" in definition['extensions']:
                        keys.append(definition['extensions']["https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/content-type"])
                    
                    if "interactionType" in definition:
                        keys.append(definition["interactionType"])

                    template = factory.get_template(*keys)()
                    contents_obj = XAPIObject(**contents["object"])
                    contents_context = XAPIContext(**contents["context"])
                    for task in template.actions():
                        t = task(
                            actor, 
                            contents_obj, 
                            contents_context
                        )
                        result, verb = t.do(attempt=self.attempt, session_id=self.session_id)
                        yield self._result_model(
                            t, actor, contents_obj, verb, result, contents_context)
            else: 
                # CMI 5일경우
                t = task(actor, lecture_object, lecture_context)
                result, verb = t.do(attempt=self.attempt)
                yield self._result_model(
                    t, actor, lecture_object, verb, result, lecture_context)

    def _result_model(self, task, actor, obj, verb, result, context):
        state = None
        stmt = XAPIStatement(
            actor=actor,
            object=obj,
            verb=verb,
            result=result,
            context=context
        )
        
        if task.has_state():
            state = XAPIState(**task.to_state())

        return stmt.to_full_statement(), state