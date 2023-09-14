from xapi_app.types.common import XAPIObjectBase


class XAPIVerb(XAPIObjectBase):
    def __init__(self):
        self.id: str
        self.self.display: dict

class LaunchedVerb(XAPIVerb): 
    def __init__(self):
        self.id =  "http://adlnet.gov/expapi/verbs/launched"
        self.display = {
            "en-US": "launched"
        }

class InitalizedVerb(XAPIVerb):
    def __init__(self):
        self.id =  "http://adlnet.gov/expapi/verbs/initialized"
        self.display = {
            "en-US": "initialized"
        }

class CompletedVerb(XAPIVerb):
    def __init__(self):
        self.id =  "http://adlnet.gov/expapi/verbs/completed"
        self.display = {
            "en-US": "completed"
        }

class PassedVerb(XAPIVerb): 
    def __init__(self):
        self.id =  "http://adlnet.gov/expapi/verbs/passed"
        self.display = {
            "en-US": "passed"
        }

class FailedVerb(XAPIVerb): 
    def __init__(self):
        self.id =  "http://adlnet.gov/expapi/verbs/failed"
        self.display = {
            "en-US": "failed"
        }

class AbandonedVerb(XAPIVerb): 
    def __init__(self):
        self.id =  "https://w3id.org/xapi/adl/verbs/abandoned"
        self.display = {
            "en-US": "abandoned"
        }

class WaivedVerb(XAPIVerb): 
    def __init__(self):
        self.id =  "https://w3id.org/xapi/adl/verbs/waived"
        self.display = {
            "en-US": "waived"
        }

class TerminatedVerb(XAPIVerb): 
    def __init__(self):
        self.id =  "http://adlnet.gov/expapi/verbs/terminated"
        self.display = {
            "en-US": "terminated"
        }

class SatisfiedVerb(XAPIVerb): 
    def __init__(self):
        self.id =  "https://w3id.org/xapi/adl/verbs/satisfied"
        self.display = {
            "en-US": "satisfied"
        }

class ReadVerb(XAPIVerb):
    def __init__(self):
        self.id =  "http://activitystrea.ms/schema/1.0/read"
        self.display = {
            "en-US": "read"
        }


class PlayedVerb(XAPIVerb):
    def __init__(self):
        self.id =  "https://w3id.org/xapi/video/verbs/played"
        self.display = {
            "en-US": "played"
        }

class SeekedVerb(XAPIVerb):
    def __init__(self):
        self.id =  "https://w3id.org/xapi/video/verbs/seeked"
        self.display = {
            "en-US": "seeked"
        }

class PausedVerb(XAPIVerb):
    def __init__(self):
        self.id =  "https://w3id.org/xapi/video/verbs/paused"
        self.display = {
            "en-US": "paused"
        }

class InteractedVerb(XAPIVerb):
    def __init__(self):
        self.id =  "http://adlnet.gov/expapi/verbs/interacted"
        self.display = {
            "en-US": "interacted"
        }

class ViewedVerb(XAPIVerb):
    def __init__(self):
        self.id =  "http://id.tincanapi.com/verb/viewed"
        self.display = {
            "en-US": "viewed"
        }

class AnsweredVerb(XAPIVerb):
    def __init__(self):
        self.id =  "http://adlnet.gov/expapi/verbs/answered"
        self.display = {
            "en-US": "answered"
        }

class DownloadedVerb(XAPIVerb):
    def __init__(self):
        self.id =  "http://id.tincanapi.com/verb/downloaded"
        self.display = {
            "en-US": "downloaded"
        }

class OpenedVerb(XAPIVerb):
    def __init__(self):
        self.id =  "https://w3id.org/xapi/netc/verbs/opened"
        self.display = {
            "en-US": "opened"
        }

class SuspendedVerb(XAPIVerb):
    def __init__(self):
        self.id =  "http://adlnet.gov/expapi/verbs/suspended"
        self.display = {
            "en-US": "suspended"
        }

class CheckedVerb(XAPIVerb):
    def __init__(self):
        self.id =  "https://w3id.org/xapi/dod-isd/verbs/checked"
        self.display = {
            "en-US": "checked"
        }
        
class SubmittedVerb(XAPIVerb):
    def __init__(self):
        self.id =  "https://w3id.org/xapi/dod-isd/verbs/submitted"
        self.display = {
            "en-US": "submitted"
        }

class ScoredVerb(XAPIVerb):
    def __init__(self):
        self.id =  "https://w3id.org/xapi/tla/verbs/scored"
        self.display = {
            "en-US": "scored"
        }

class AssessedVerb(XAPIVerb):
    def __init__(self):
        self.id =  "https://w3id.org/xapi/dod-isd/verbs/assessed"
        self.display = {
            "en-US": "assessed"
        }