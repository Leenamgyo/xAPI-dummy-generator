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

    def start(self, **kwargs):
        self.result =  XAPIResult(
            success=True,
            completion=True,
            duration=iso8601.parse_sec_to_duration(random.randint(3,5)),
            extensions={
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt": kwargs["attempt"],
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid": kwargs["session_id"]
            }
        )
    
class Answered(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=AnsweredVerb(),
            context=context
        )

    def start(self, **kwargs):
        score_max = 100
        score_min = 0
        score_raw = random.randint(20, 100)

        self.result =  XAPIResult(
            success=True,
            completion=True,
            duration=iso8601.parse_sec_to_duration(random.randint(3,5)),
            score={
                "max": score_max,
                "min": score_min,
                "raw": random.randint(20, 100),
                "scaled": score_raw/score_max
            },
            extensions={
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt": kwargs["attempt"],
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid": kwargs["session_id"]
            }
        )
    
        return self.result.score