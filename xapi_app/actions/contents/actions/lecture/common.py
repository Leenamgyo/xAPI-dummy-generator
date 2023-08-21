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
            extensions={
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt": kwargs["attempt"],
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid ": kwargs["session_id"]
            }
        )


