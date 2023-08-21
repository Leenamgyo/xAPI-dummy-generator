import time
import uuid
import random
import os 
from locust import HttpUser, TaskSet, task, between

from xapi_app.scenario import Cmi5Scenario
from xapi_app.utils import file


# TODO: Locust user의 instance 수와 actor을 매칭할 수 있으면 actor의 수대로 실행이 가능해서 attmpt 관리가 가능하다

def set_actor():
    return file.load_json("resources/2023-08-20/actors.json")

def set_object_extensions():
    list_ = []
    lecture_path = "resources/2023-08-20/lecture"
    content_path = "resources/2023-08-20/contents"
    for lecture_name in os.listdir(lecture_path):
        lecture = file.load_json(lecture_path+"/"+lecture_name)
        contents = file.load_json(content_path+"/"+lecture_name)
        list_.append(lecture, contents)
    
    return list_

class User(HttpUser):
    wait_time = between(1, 5)
    _actors = set_actor()
    _object_extensions = set_object_extensions()

    @task
    def task_1(self):
        session_id = uuid.uuid4()
        attempt = random.randint(1, 3)
        object_extensions = self._get_object_extensions()
        scenario = Cmi5Scenario(
            session_id=session_id,
            attempt=attempt,
            actor=self._get_actor(),
            lecture_object_context=object_extensions[0],
            contents_object_context=object_extensions[1]
        )
        
        for full_statement, state in scenario.run_complted_with_contents():
            if state:
                self._state_api_request("POST", "/xAPI/activities/state", body=state.body(), params=state.param())
            return self._api_request("POST", "/xAPI/statements", full_statement)

    def _get_actor(self):
        return self._actor[random.randint(1, 100) % len(self._actor)]

    def _get_object_extensions(self):
        return self._object_extensions[random.randint(1, 100) % len(self._object_extensions)] 

    def _auth_header(self):
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Authorization": "Basic Og==",
            "X-Experience-API-Version": "1.0.3",
            "Accept": "*/*",
            "Host": "cne-lrs.bubblecon.io",
        }
        return headers

    def _api_request(self, method, url, body=None):
        return self.client.request(
            method,
            url,
            json=body,
            headers=self._auth_header(),
        )

    def _state_api_request(self, method, url, body=None, params=None):
        return self.client.request(
            method,
            url,
            json=body,
            headers=self._auth_header(),
            params=params,
        )
