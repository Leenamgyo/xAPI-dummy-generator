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

class Submitted(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=SubmittedVerb(),
            context=context
        )

    def start(self, **kwargs):
        self.result =  XAPIResult(
            success=True,
            completion=True,
            response="",
            duration=iso8601.parse_sec_to_duration(random.randint(1, 3)),
            extensions={
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid": kwargs["session_id"],
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt": kwargs["attempt"]
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
            duration=iso8601.parse_sec_to_duration(random.randint(5, 10)),
            score={},
            extensions={
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid": kwargs["session_id"],
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt": kwargs["attempt"]
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
            "submit_timestamp": iso8601.timestamp_now_str(),
            "is_assessed": "false"
        }
           
        return params, body

    

class Scoreded(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=ScoredVerb(),
            context=context
        )

    def start(self, **kwargs):
        min_ = 0
        max_ = 5
        raw_ = random.randint(1, 5)
        scaled = raw_ / max_
        self.result =  XAPIResult(
            success=True,
            completion=True,
            response="짧은 시간에 이 프로젝트를 시작했을 때 여러분 모두가 해주신 놀라운 작업에 감사드립니다. 우리 모두가 한 팀으로 일하는 모습이 놀랍습니다.",
            score={
                "min": 0,
                "max": 5,
                "raw": raw_,
                "scaled": scaled
            },
            extensions={
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid": kwargs["session_id"],
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt": kwargs["attempt"]
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
            "instructor_score": random.randint(30, 100),
            "is_assessed": "true"
        }
            
        return params, body

    
