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
        
    def do(self, duration=None):
        return None, self.verb
    

class Completed(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=CompletedVerb(),
            context=context
        )

    def do(self, duration):
        result = XAPIResult(
            success=True,
            completion=True,
            duration=iso8601.parse_sec_to_duration(random.randint(3,7)),
            extensions=None
        )

        return result, self.verb


class Played(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=PlayedVerb(),
            context=context
        )
    
    def do(self, session_id, duration=None, attempt=None):
        result = XAPIResult(
            success=True,
            extensions={
                "https://w3id.org/xapi/video/extensions/session-id": session_id,
                "https://w3id.org/xapi/video/extensions/time":"",
                "https://w3id.org/xapi/video/extensions/played-segments":""
            }
        )
        return result

class Seeked(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=SeekedVerb(),
            context=context
        )

    def do(self, duration, attempt, session_id):
        result = XAPIResult(
            success=True,
            extensions={
                "https://w3id.org/xapi/video/extensions/session-id": "",
                "https://w3id.org/xapi/video/extensions/time-from": "",
                "https://w3id.org/xapi/video/extensions/time-to": ""
            }
        )
        return result
class Paused(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=PausedVerb(),
            context=context
        )

    def do(self, duration, attempt, session_id):
        result = XAPIResult(
            success=True,
            duration=duration,
            extensions={
                "https://w3id.org/xapi/video/extensions/session-id":"",
                "https://w3id.org/xapi/video/extensions/time":"",
                "https://w3id.org/xapi/video/extensions/played-segments":"",
                "https://w3id.org/xapi/video/extensions/progress":""
            }
        )
        return result
    
class Interacted(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=InteractedVerb(),
            context=context
        )

    def do(self, duration, attempt, session_id):
        result = XAPIResult(
            success=True,
            extensions={
                "https://w3id.org/xapi/video/extensions/session-id":"",
                "https://w3id.org/xapi/video/extensions/full-screen":"",
                "https://w3id.org/xapi/video/extensions/speed":"",
                "https://w3id.org/xapi/video/extensions/volume":"",
            }
        )
        return result
    
class Viewed(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=ViewedVerb(),
            context=context
        )

    def do(self, duration, attempt, session_id):
        result = XAPIResult(
            duration=duration,
            extensions={
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid":"",
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt":""
            }
        )
        return result

class Donwloaded(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=DownloadedVerb(),
            context=context
        )

    def do(self, duration, attempt, session_id):
        result = XAPIResult(
            duration=duration,
            extensions={
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid":""
            }
        )

class Answered(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=AnsweredVerb(),
            context=context
        )

    def do(self, duration, attempt, session_id):
        result = XAPIResult(
            success=True,
            completion=True,
            response="",
            duration=duration,
            score={},
            extensions={
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid":"",
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt":""
            }
        )
        return result



class Opened(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=OpenedVerb(),
            context=context
        )

    def do(self, duration, attempt, session_id):
        result = XAPIResult(
            success=True,
            completion=True,
            duration=duration,
            extensions={
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid":""
            }
        )
        return result


class Checked(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=CheckedVerb(),
            context=context
        )

    def do(self, duration, attempt, session_id):
        result = XAPIResult(
            success=True,
            completion=True,
            response="",
            duration=duration,
            score="",
            extensions={
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid":"",
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt":""
            }
        )
        return result
    

class Scored(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=ScoredVerb(),
            context=context
        )

    def do(self, duration, attempt, session_id):
        result = XAPIResult(
            success=True,
            completion=True,
            response="",
            score="",
            extensions={
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid":"",
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt":""
            }
        )
        return result
    

class Submitted(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=SubmittedVerb(),
            context=context
        )

    def do(self, duration, attempt, session_id):
        result = XAPIResult(
            success=True,
            completion=True,
            response="",
            duration=duration,
            extensions={
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid":"",
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt":""
            }
        )

        return result
    
