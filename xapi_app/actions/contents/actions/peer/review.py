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

class Assessed(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=AssessedVerb(),
            context=context
        )

    def start(self, **kwargs):
        max_ = 100
        min_ = 0
        raw_ = 0
        raw_ = random.randint(1, 100)

        self.result =  XAPIResult(
            success=True,
            completion=True,
            response="저는 오늘 귀하가 그 어려운 고객 전화를 어떻게 처리했는지에 대해 제가 얼마나 감명을 받았는지 말씀드리고 싶습니다. 당신은 시종일관 차분하고 프로페셔널했으며, 소비자가 만족하는 상황을 해결할 수 있었습니다. 바로 당신이 우리 팀을 돋보이게 만드는 것입니다.",
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
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/assessed/content/id": kwargs["content_id"]
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
            "max_score": self.result.score["max"],
            "score": self.result.score["raw"]
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
            response="짧은 시간에 이 프로젝트를 시작했을 때 여러분 모두가 해주신 놀라운 작업에 감사드립니다. 우리 모두가 한 팀으로 일하는 모습이 놀랍습니다.",
            duration=iso8601.parse_sec_to_duration(random.randint(5, 10)),
            score={},
            extensions={
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid": kwargs["session_id"],
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt": kwargs["attempt"],
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/assessed/content/id": kwargs["content_id"]
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
        max_ = 100
        min_ = 0
        raw_ = 0
        raw_ = random.randint(1, 100)

        self.result =  XAPIResult(
            success=True,
            completion=True,
            response='프로젝트를 제시간에 고품질로 완료하기 위해 정말 열심히 노력했습니다! 세부 사항에 대한 관심과 마감일을 맞추기 위한 노력은 정말 인상적입니다. 당신은 프로젝트의 성공에 크게 기여했으며 우리 팀에 당신이 있어 감사합니다.',
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
            "instructor_score": self.result.score["raw"],
            "submit_timestamp": iso8601.timestamp_now_str(),
            "is_assessed": "true"
        }
            
        return params, body
    