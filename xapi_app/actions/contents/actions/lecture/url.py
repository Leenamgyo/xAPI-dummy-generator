import random

from xapi_app.types import *
from xapi_app.actions.common import XAPIAction
from xapi_app.types import XAPIResult

from xapi_app.utils import iso8601


class Opened(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=OpenedVerb(),
            context=context
        )

    def start(self, **kwargs):
        self.result =  XAPIResult(
            success=True,
            completion=True,
            duration=iso8601.parse_sec_to_duration(5, 7),
            extensions={
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid": kwargs["session_id"]
            }
        )
