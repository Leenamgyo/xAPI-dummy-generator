import random

from xapi_app.types import *
from xapi_app.actions.common import XAPIAction
from xapi_app.types import XAPIResult

from xapi_app.utils import iso8601

class Read(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=ReadVerb(),
            context=context
        )
    
    def do(self, attempt, session_id, duration=None):
        result = XAPIResult(
            duration=iso8601.parse_sec_to_duration(random.randint(3,7)),
            extensions={
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt": attempt,
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid": session_id
            }
        )
        return result, self.verb