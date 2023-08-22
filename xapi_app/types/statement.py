from xapi_app.types.common import XAPIObjectBase
from xapi_app.types.actor import XAPIActor
from xapi_app.types.obj import XAPIObject
from xapi_app.types.verb import XAPIVerb

class XAPIStatement:
    def __init__(
        self, 
        verb,
        result,
        actor, 
        object,
        context,
        version="1.0.3"
    ):
        self.verb = verb
        self.version = version 
        self.actor = actor
        self.object = object
        self.result =  result
        self.context = context

    def to_full_statement(self):
        stmt = {
            "version": self.version,
            "verb": self.verb.result_dict(),
            "object": self.object.result_dict(),
            "actor": self.actor.result_dict(),
            "context": self.context.result_dict()
        }
        if self.result:
            stmt["result"] = self.result.result_dict()
        return stmt
    
    
        

    
    