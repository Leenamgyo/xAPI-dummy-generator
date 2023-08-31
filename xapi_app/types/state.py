class XAPIState:
    def __init__(
        self,
        params,
        body
    ):
        self.params = params
        self.body = body
    def get_params(self):
        return self.params

    def get_body(self):
        return self.body