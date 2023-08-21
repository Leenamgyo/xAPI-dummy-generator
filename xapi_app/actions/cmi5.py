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
            success='true',
            completion='true',
            duration=iso8601.parse_sec_to_duration(random.randint(3,7)),
            score=kwargs["total_score"],
            extensions={
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt": kwargs["attempt"],
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/session_time": iso8601.parse_sec_to_duration(random.randint(1000, 3000))
            }
        )
        

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
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/session_time":iso8601.parse_sec_to_duration(random.randint(1000, 3000))
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


