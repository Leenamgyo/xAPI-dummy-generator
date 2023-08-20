from xapi_app.types.common import XAPIObjectBase

class XAPIActor(XAPIObjectBase):
    def __init__(self, name, objectType, account):
        self.name = name
        self.objectType = objectType
        self.account = account
