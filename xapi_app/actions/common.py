from typing import Union

from xapi_app.types import XAPIActor, XAPIResult, XAPIVerb, XAPIObject, XAPIContext

class XAPIAction:
    def __init__(
        self, 
        *,
        actor: XAPIActor, 
        verb: XAPIVerb,
        obj: XAPIObject, 
        context: XAPIContext,
        result: XAPIResult
    ):
        self.actor = actor
        self.obj = obj
        self.context = context
        self.verb = verb
        self.self.result =  result

    def start(self, **kwargs):
        raise NotImplementedError

    def has_state(self):
        return False

    def to_state(self, **kwargs):
        raise NotImplementedError

