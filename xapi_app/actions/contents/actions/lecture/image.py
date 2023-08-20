import random

from xapi_app.types import *
from xapi_app.actions.common import XAPIAction
from xapi_app.types import XAPIResult

from xapi_app.utils import iso8601

class Viewed(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=ViewedVerb(),
            context=context
        )

    def start(self, **kwargs):
        self.result =  XAPIResult(
            duration=iso8601.parse_sec_to_duration(random.randint(3, 20)),
            extensions={
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid": session_id,
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt":attempt
            }
        )
