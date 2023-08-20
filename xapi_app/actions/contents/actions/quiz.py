import random

from xapi_app.types import *
from xapi_app.actions.common import XAPIAction
from xapi_app.types import XAPIResult

from xapi_app.utils import iso8601

class Completed(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=CompletedVerb(),
            context=context
        )

    def do(self, duration):
        result = XAPIResult(
            success=True,
            completion=True,
            duration=iso8601.parse_sec_to_duration(random.randint(3,7)),
            score={},
            extensions={
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt": "",
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid": ""
            }
        )

        return result