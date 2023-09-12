import random

from xapi_app.types import LaunchedVerb, InitalizedVerb, PassedVerb, CompletedVerb, FailedVerb, AbandonedVerb, WaivedVerb, TerminatedVerb, SatisfiedVerb
from xapi_app.actions.common import XAPIAction
from xapi_app.types import XAPIResult
from xapi_app.utils import iso8601


class Launched(XAPIAction):  
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=LaunchedVerb(),
            context=context
        )
        
    def start(self, **kwargs):
        self.result = None

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

    def has_state(self):
        return True 
    
    def to_state(self):
        agent_id = self.actor.account["homePage"][self.actor.account["homePage"].rindex("/") + 1 :]
        total_time = random.randrange(1, 1000)
        attempt = random.randint(1, 3)

        params = {
            "agent": self.actor.result_json(),
            "activityId": self.obj.id,
            "stateId": f"{self.obj.id}/{agent_id}",
        }
    
        body = {
            "initial_timestamp": iso8601.timestamp_now_str(),
            "complete_timestamp": iso8601.timestamp_now_str(),
            "attempt": attempt,
            "total_time": random.randint(1, 1000),
            "avg_attempt_times": total_time / attempt
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
        max_ = 100
        min_ = 0
        raw_ = random.randint(30, 60)
        scaled_ = raw_/max_
        self.result =  XAPIResult(
            success=True,
            completion=True,
            duration=iso8601.parse_sec_to_duration(random.randint(3,7)),
            score={
                "max": max_,
                "min": min_,
                "raw": raw_,
                "scaled": scaled_
            },
            extensions={
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt": kwargs["attempt"],
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/session_time": iso8601.parse_sec_to_duration(random.randint(1000, 3000))
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
            "initial_timestamp": iso8601.timestamp_now_str(),
            "complete_timestamp": iso8601.timestamp_now_str(),
            "attempt": attempt,
            "total_time": total_time,
            "avg_attempt_times": total_time / attempt
        }

        if self.result.score:
            body["score"] = self.result.score["raw"]
            body["max_score"] = 100
            
        return params, body
        

class Passed(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=PassedVerb(),
            context=context
        )

    def start(self, **kwargs):
        self.result = None
    

class Failed(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=FailedVerb(),
            context=context
        )

    def start(self, **kwargs):
        self.result =  XAPIResult(
            success=False,
            duration=iso8601.parse_sec_to_duration(random.randint(3,7)),
            extensions={
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/session_time": iso8601.parse_sec_to_duration(random.randint(1000, 3000))
            }
        )

class Aboandoned(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=AbandonedVerb(),
            context=context
        )

    def start(self, **kwargs):
        self.result =  XAPIResult(
            duration=iso8601.parse_sec_to_duration(random.randint(3,7)),
        )


class Waived(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=WaivedVerb(),
            context=context
        )

    def start(self, **kwargs):
        self.result =  XAPIResult(
            success=True,
            completion=True,
            duration=iso8601.parse_sec_to_duration(random.randint(3,7)),
            extensions={
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/session_time": iso8601.parse_sec_to_duration(random.randint(1000, 3000))
            }
        )


class Terminated(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=TerminatedVerb(),
            context=context
        )

    def start(self, **kwargs):
        self.result =  XAPIResult(
            duration=iso8601.parse_sec_to_duration(random.randint(3,7)),
            extensions={
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/session_time":iso8601.parse_sec_to_duration(random.randint(1000, 3000))
            }
        )
        

class Satisfied(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=SatisfiedVerb(),
            context=context
        )


    def start(self, **kwargs):
        self.result =  XAPIResult(
            duration=iso8601.parse_sec_to_duration(random.randint(3,7)),
            score={},
            extensions={
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/session_time": iso8601.parse_sec_to_duration(random.randint(1000, 3000))
            }
        )


