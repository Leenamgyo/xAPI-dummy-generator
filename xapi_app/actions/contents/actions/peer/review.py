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
    def has_state(self):
        return True
    
    def to_state(self):
        agent_id = self.actor.account["homePage"][self.actor.account["homePage"].rindex("/") + 1 :]

        params = {
            "agent": self.actor.result_json(),
            "activityId": self.obj.id,
            "stateId": f"{self.obj.id}/{agent_id}",
        }
        
        total_time = random.randrange(1, 1000)
        attempt = self.result.extensions["https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt"]
        
        body = {
            "attempt": attempt,
            "total_time": total_time,
            "avg_attempt_times": total_time / attempt,
            "is_assessed": "none"
        }
            
        return params, body


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
