import random

from xapi_app.types import *
from xapi_app.actions.common import XAPIAction
from xapi_app.types import XAPIResult

from xapi_app.utils import inputs, iso8601

class Answered(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=AnsweredVerb(),
            context=context
        )

    def do(self, duration, attempt, session_id):
        result = XAPIResult(
            success="true",
            completion="true",
            response=str(random.randint(1,4)),
            duration=iso8601.parse_sec_to_duration(random.randint(3, 5)),
            extensions={
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid": session_id
            }
        )
        return result