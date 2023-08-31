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

class Acceessed(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=AccessedVerb(),
            context=context
        )

    def start(self, **kwargs):
        max_ = 250
        min_ = 0
        raw_ = 0
        raw_ = random.randint(1, 250)

        self.result =  XAPIResult(
            success=True,
            completion=True,
            response="",
            duration=iso8601.parse_sec_to_duration(random.randint(1, 3)),
            score={
                "max": max_,
                "min": min_,
                "raw": raw_,
                "scaled": raw_ / max_
            },
            extensions={
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid": kwargs["session_id"],
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt": kwargs["attempt"],
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/accessed/content/id": kwargs["content_id"]
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
        self.result =  XAPIResult(
            success=True,
            completion=True,
            response="",
            duration=iso8601.parse_sec_to_duration(random.randint(5, 10)),
            score={},
            extensions={
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid": kwargs["session_id"],
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt": kwargs["attempt"],
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/accessed/content/id": kwargs["content_id"]
            }
        )
    

class Scoreded(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=ScoredVerb(),
            context=context
        )

    def start(self, **kwargs):
        max_ = 250
        min_ = 0
        raw_ = 0
        raw_ = random.randint(1, 250)

        self.result =  XAPIResult(
            success=True,
            completion=True,
            response="Scored",
            score={
                "max": max_,
                "min": min_,
                "raw": raw_,
                "scaled": raw_ / max_
            },
            extensions={
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid": kwargs["session_id"],
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt": kwargs["attempt"]
            }
        )
