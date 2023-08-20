import random

from xapi_app.types import *
from xapi_app.actions.common import XAPIAction
from xapi_app.types import XAPIResult

from xapi_app.utils import iso8601

class Interacted(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=InteractedVerb(),
            context=context
        )

    def do(self, attempt, session_id, duration=None):
        result = XAPIResult(
            success="true",
            completion="true",
            duration=iso8601.parse_sec_to_duration(random.randint(3,5)),
            extensions={
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid": session_id,
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt": attempt
            }
        )
        return result
    
class Answered(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=AnsweredVerb(),
            context=context
        )

    def do(self, attempt, session_id, duration=None):
        result = XAPIResult(
            success="true",
            completion="true",
            duration=iso8601.parse_sec_to_duration(random.randint(3,5)),
            score={},
            extensions={
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid": session_id,
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt": attempt
            }
        )
        return result
    