import random

from xapi_app.types import *
from xapi_app.actions.common import XAPIAction
from xapi_app.types import XAPIResult

from xapi_app.utils import iso8601

class Initialized(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=InitalizedVerb(),
            context=context
        )
        
    def start(self, **kwargs):
        self.result = None

class Suspended(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=SuspendedVerb(),
            context=context
        )

    def start(self, **kwargs):
        self.result =  XAPIResult(
            success=str('true'),
            completion=str('true'),
            duration=iso8601.parse_sec_to_duration(random.randint(1, 3)),
            extensions={
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt": kwargs["attempt"],
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid ": kwargs["session_id"]
            }
        )


class Checked(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=CheckedVerb(),
            context=context
        )

    def start(self, **kwargs):
        score_max = 5
        score_min = 0
        score_raw = random.randint(1, 5)
        response = random.randint(1, 4)

        self.result =  XAPIResult(
            success=str('true'),
            completion=str('true'),
            response=response,
            duration=iso8601.parse_sec_to_duration(random.randint(1, 3)),
            score={
                "max": score_max,
                "min": score_min,
                "raw": score_raw,
                "scaled": score_raw/score_max
            },
            extensions={
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt": kwargs["attempt"],
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid ": kwargs["session_id"]
            }
        )


class Completed(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=CompletedVerb(),
            context=context
        )

    def start(self, **kwargs):
        score_max = 5
        score_min = 0
        score_raw = random.randint(1, 5)
        response = "서술형"

        self.result =  XAPIResult(
            success="true",
            completion="true",
            duration=iso8601.parse_sec_to_duration(random.randint(3,5)),
            response=response,
            score={
                "max": score_max,
                "min": score_min,
                "raw": score_raw,
                "scaled": score_raw/score_max
            },
            extensions={
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt": kwargs["attempt"],
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid ": kwargs["session_id"]
            }
        )
        return self.result.score


class Answered(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=AnsweredVerb(),
            context=context
        )

    def start(self, **kwargs):
        score_max = 5
        score_min = 0
        score_raw = random.randint(1, 5)
        response = random.randint(1, 4)

        self.result =  XAPIResult(
            success="true",
            completion="true",
            duration=iso8601.parse_sec_to_duration(random.randint(3,5)),
            response=response,
            score={
                "max": score_max,
                "min": score_min,
                "raw": score_raw,
                "scaled": score_raw/score_max
            },
            extensions={
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt": kwargs["attempt"],
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid ": kwargs["session_id"]
            }
        )
   

class Scored(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=ScoredVerb(),
            context=context
        )

    def start(self, **kwargs):
        score_max = 5
        score_min = 0
        score_raw = random.randint(1, 5)
        response = random.randint(1, 4)

        self.result =  XAPIResult(
            success=str('true'),
            completion=str('true'),
            response="서술형",
            score={
                "max": score_max,
                "min": score_min,
                "raw": score_raw,
                "scaled": score_raw/score_max
            },
            extensions={
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt": kwargs["attempt"],
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid ": kwargs["session_id"]
            }
        )
