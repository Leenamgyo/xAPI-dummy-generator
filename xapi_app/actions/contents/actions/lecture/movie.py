import random

from xapi_app.types import *
from xapi_app.actions.common import XAPIAction
from xapi_app.types import XAPIResult

from xapi_app.utils import iso8601

class Played(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=PlayedVerb(),
            context=context
        )
    
    def start(self, **kwargs):
        self.result =  XAPIResult(
            success=True,
            extensions={
                "https://w3id.org/xapi/video/extensions/session-id": kwargs["session_id"],
                "https://w3id.org/xapi/video/extensions/time":0,
                "https://w3id.org/xapi/video/extensions/played-segments": self.plus_segment()
            }
        )
    
    def plus_segment(self):
        """
        Compare the new segment with to object["definition"]["extensions"]["https://w3id.org/xapi/video/activity-type/video/duration"] property,
        add new one to the exists segments. if false, reset segments
        """
        segments = "null[.]4.954"
        play_lst = float(segments.split("[.]")[-1])
        play_plus = play_lst + random.randrange(1, 100)

        object_time = int(
            self.obj.definition["extensions"]["https://w3id.org/xapi/video/activity-type/video/duration"]
        )
        
        if not play_plus > object_time:
            segments = f"{segments}[,]{play_lst}[.]{play_plus}"
        else:
            segments = f"null[.]{random.randrange(1,10)}.{random.randrange(1,100)}"
        return segments


    
class Seeked(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=SeekedVerb(),
            context=context
        )

    def start(self, **kwargs):
        random_time_from = random.randrange(1, 100)
        random_time_to = random_time_from + random.randrange(1, 100)
        
        self.result =  XAPIResult(
            success=True,
            extensions={
                "https://w3id.org/xapi/video/extensions/session-id": kwargs["session_id"],
                "https://w3id.org/xapi/video/extensions/time-from": random_time_from,
                "https://w3id.org/xapi/video/extensions/time-to": random_time_to
            }
        )


class Paused(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=PausedVerb(),
            context=context
        )

    def start(self, **kwargs):
        self.result =  XAPIResult(
            success=True,
            duration=iso8601.parse_sec_to_duration(5),
            extensions={
                "https://w3id.org/xapi/video/extensions/session-id": kwargs["session_id"],
                "https://w3id.org/xapi/video/extensions/time": random.randrange(1, 400),
                "https://w3id.org/xapi/video/extensions/played-segments": self.plus_segment(),
                "https://w3id.org/xapi/video/extensions/progress": 0.123
            }
        )

    def plus_segment(self):
        """
        Compare the new segment with to object["definition"]["extensions"]["https://w3id.org/xapi/video/activity-type/video/duration"] property,
        add new one to the exists segments. if false, reset segments
        """
        segments = "null[.]4.954"
        play_lst = float(segments.split("[.]")[-1])
        play_plus = play_lst + random.randrange(1, 100)

        object_time = int(
            self.obj.definition["extensions"]["https://w3id.org/xapi/video/activity-type/video/duration"]
        )
        
        if not play_plus > object_time:
            segments = f"{segments}[,]{play_lst}[.]{play_plus}"
        else:
            segments = f"null[.]{random.randrange(1,10)}.{random.randrange(1,100)}"
        return segments

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
        attempt = random.randint(1, 3)
        
        body = {
            "played_segments": self.result.extensions["https://w3id.org/xapi/video/extensions/played-segments"],
            "time": self.result.extensions["https://w3id.org/xapi/video/extensions/time"],
            "progress": self.result.extensions["https://w3id.org/xapi/video/extensions/progress"],
            "attempt": attempt,
            "total_time": total_time,
            "avg_attempt_times": float(total_time / attempt)
        }
            
        return params, body

    
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
            extensions={
                "https://w3id.org/xapi/video/extensions/session-id": kwargs["session_id"],
                "https://w3id.org/xapi/video/extensions/full-screen": "false",
                "https://w3id.org/xapi/video/extensions/speed": "1",
                "https://w3id.org/xapi/video/extensions/volume": random.randint(1, 25),
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
            duration=iso8601.parse_sec_to_duration(random.randint(3,7)),
            score={},
            extensions={
                "https://w3id.org/xapi/video/extensions/session-id": kwargs["session_id"],
                "https://w3id.org/xapi/video/extensions/time": random.randrange(1, 600),
                "https://w3id.org/xapi/video/extensions/progress": 0.123,
                "https://w3id.org/xapi/video/extensions/played-segments": self.plus_segment()
            }
        )
    
    def plus_segment(self):
        """
        Compare the new segment with to object["definition"]["extensions"]["https://w3id.org/xapi/video/activity-type/video/duration"] property,
        add new one to the exists segments. if false, reset segments
        """
        segments = "null[.]4.954"
        play_lst = float(segments.split("[.]")[-1])
        play_plus = play_lst + random.randrange(1, 100)

        object_time = int(
            self.obj.definition["extensions"]["https://w3id.org/xapi/video/activity-type/video/duration"]
        )
        
        if not play_plus > object_time:
            segments = f"{segments}[,]{play_lst}[.]{play_plus}"
        else:
            segments = f"null[.]{random.randrange(1,10)}.{random.randrange(1,100)}"
        return segments


