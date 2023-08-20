from xapi_app.types.common import XAPIObjectBase

class XAPIState:
    def __init__(
        self,
        actor,
        obj,
        progress=None,
        played_segments=None,
        time=None,
        total_time=None,
        avg_attempt_time=None,
        score=None,
        instructor_score=None,
        is_assessed=None,
        initial_timestamp=None,
        complete_timestamp=None
    ):
        self.actor = actor,
        self.obj = obj,
        self.progress = progress   
        self.plyed_segments = played_segments,
        self.time = time
        self.total_time = total_time
        self.avg_attempt_time = avg_attempt_time
        self.score = score
        self.instructor_score = instructor_score
        self.is_assessed = is_assessed,
        self.initial_timestamp = initial_timestamp
        self.complete_timestamp = complete_timestamp

    def params(self):
        pass

    def body(self):
        body_ = {}

        if self.plyed_segments:
            body_["played_segments"] = self.plyed_segments

    def validate(self):
        pass