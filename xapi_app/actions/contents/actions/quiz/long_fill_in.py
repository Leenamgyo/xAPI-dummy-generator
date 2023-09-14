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
            success=True,
            completion=True,
            duration=iso8601.parse_sec_to_duration(random.randint(1, 3)),
            extensions={
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt": kwargs["attempt"],
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid": kwargs["session_id"]
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
        response = "서술형 답"
        
        if score_raw == score_max:
            response = ",".join(self.obj.definition["correctResponsesPattern"])

        self.result =  XAPIResult(
            success=True,
            completion=True,
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
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid": kwargs["session_id"]
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
        response = "fail"
        if score_raw == score_max:
            response = ",".join(self.obj.definition["correctResponsesPattern"])

        self.result =  XAPIResult(
            success=True,
            completion=True,
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
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid": kwargs["session_id"]
            }
        )
        return self.result.score
    
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
            "is_assessed": "false"
        }
            
        return params, body


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
        response = "fail"
        if score_raw == score_max:
            response = ",".join(self.obj.definition["correctResponsesPattern"])        

        self.result =  XAPIResult(
            success=True,
            completion=True,
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
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid": kwargs["session_id"]
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
        response = "fail"
        if score_raw == score_max:
            response = ",".join(self.obj.definition["correctResponsesPattern"])

        self.result =  XAPIResult(
            success=True,
            completion=True,
            response=response,
            score={
                "max": score_max,
                "min": score_min,
                "raw": score_raw,
                "scaled": score_raw/score_max
            },
            extensions={
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt": kwargs["attempt"],
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid": kwargs["session_id"]
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
            "is_assessed": "true",
            "instructor_score": random.randint(1, 5)
        }
        
        return params, body
