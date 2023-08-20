from xapi_app.types.common import XAPIObjectBase

class XAPIResult(XAPIObjectBase):
    def __init__(
            self, 
            success=None,
            completion=None,
            duration=None,
            score=None
            ,
            response=None,
            extensions=None
        ):
        self.success = success
        self.completion = completion
        self.response: str = response
        self.duration: str = duration
        self.score: dict = score
        self.extensions: dict = extensions

    