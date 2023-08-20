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
        
    def do(self, attempt, session_id, duration=None):
        return None, self.verb
    

class Completed(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=CompletedVerb(),
            context=context
        )

    def do(self, attempt, session_id, duration=None):
        result = XAPIResult(
            success='true',
            completion='true',
            duration=iso8601.parse_sec_to_duration(random.randint(3,7)),
            extensions=None
        )

        return result, self.verb

