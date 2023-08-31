import json 

class XAPIObjectBase:    
    def result_dict(self): 
        dict_ = {k: v for k,v in self.__dict__.items() if v is not None}
        return dict_

    def result_json(self) -> json:
        return json.dumps(self.result_dict())
    
    def validate(self):
        pass
            

    # def _check_allowed_property(self):
        

