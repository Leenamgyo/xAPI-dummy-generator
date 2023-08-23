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
                "https://w3id.org/xapi/video/extensions/time":"",
                "https://w3id.org/xapi/video/extensions/played-segments":""
            }
        )

class Seeked(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=SeekedVerb(),
            context=context
        )

    def start(self, **kwargs):
        self.result =  XAPIResult(
            success=True,
            extensions={
                "https://w3id.org/xapi/video/extensions/session-id": "",
                "https://w3id.org/xapi/video/extensions/time-from": "",
                "https://w3id.org/xapi/video/extensions/time-to": ""
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
            duration=duration,
            extensions={
                "https://w3id.org/xapi/video/extensions/session-id":"",
                "https://w3id.org/xapi/video/extensions/time":"",
                "https://w3id.org/xapi/video/extensions/played-segments":"",
                "https://w3id.org/xapi/video/extensions/progress":""
            }
        )
    
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
                "https://w3id.org/xapi/video/extensions/session-id": session_id,
                "https://w3id.org/xapi/video/extensions/full-screen":"false",
                "https://w3id.org/xapi/video/extensions/speed":"1",
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
                "https://w3id.org/xapi/video/extensions/session-id": "",
                "https://w3id.org/xapi/video/extensions/time": "",
                "https://w3id.org/xapi/video/extensions/progress": "",
                "https://w3id.org/xapi/video/extensions/played-segments": ""
            }
        )

