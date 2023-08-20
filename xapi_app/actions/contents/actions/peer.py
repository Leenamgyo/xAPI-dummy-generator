import random

from xapi_app.types import *
from xapi_app.actions.common import XAPIAction
from xapi_app.types import XAPIResult

from xapi_app.utils import iso8601

class Accessed(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=AccessedVerb(),
            context=context
        )

    def do(self, duration, attempt, session_id):
        result = XAPIResult(
            success=True,
            completion=True,
            response="",
            duration=duration,
            score={},
            extensions={
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid":"",
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt":"",
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/accessed/content/id": ""
            }
        )

        return result