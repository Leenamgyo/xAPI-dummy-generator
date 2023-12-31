from xapi_app.types.common import XAPIObjectBase

import uuid 

class XAPIContext(XAPIObjectBase):
    def __init__ (
            self,
            instructor,
            team,
            platform,
            contextActivities,
            extensions=None,
            registration=None,
            revision=None
        ):
        self.instructor = instructor
        self.team = team
        self.registration = str(uuid.uuid4())
        self.revision = "1.0"
        self.platform = platform
        self.contextActivities = contextActivities
        self.extensions = extensions

    # id: str
    # display: dict
