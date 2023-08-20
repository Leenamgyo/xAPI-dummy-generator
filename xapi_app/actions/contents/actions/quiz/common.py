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

class Suspended(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=SuspendedVerb(),
            context=context
        )

    def do(self, duration, attempt, session_id):
        result = XAPIResult(
            success=str('true'),
            completion=str('true'),
            duration=iso8601.parse_sec_to_duration(random.randint(1, 3)),
            extensions={
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid": session_id,
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt": attempt
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
            success=str('true'),
            completion=str('true'),
            response="",
            duration=iso8601.parse_sec_to_duration(random.randint(1, 3)),
            score={},
            extensions={
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid": session_id,
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt": attempt
            }
        )
        return result



class Completed(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=CompletedVerb(),
            context=context
        )

    def do(self, duration, attempt, session_id):
        result = XAPIResult(
            success=str('true'),
            completion=str('true'),
            duration=iso8601.parse_sec_to_duration(random.randint(5, 10)),
            score={},
            extensions={
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid": session_id,
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt": attempt
            }
        )
        return result


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
            success=str('true'),
            completion=str('true'),
            response="",
            duration=iso8601.parse_sec_to_duration(random.randint(5, 10)),
            score={},
            extensions={
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid": session_id,
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt": attempt
            }
        )
        return result
    

class Scoreded(XAPIAction):
    def __init__(self, actor, obj, context):
        super().__init__(
            actor=actor, 
            obj=obj, 
            verb=ScoredVerb(),
            context=context
        )

    def do(self, duration, attempt, session_id):
        result = XAPIResult(
            success=str('true'),
            completion=str('true'),
            response="",
            score={},
            extensions={
                "https://w3id.org/xapi/cmi5/context/extensions/sessionid": session_id,
                "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/attempt": attempt
            }
        )
        return result
