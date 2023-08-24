import time
import uuid
import random
import os 
from locust import HttpUser, TaskSet, task, between

from xapi_app.scenario import Cmi5Scenario
from xapi_app.utils import file

from copy import deepcopy


# TODO: Locust user의 instance 수와 actor을 매칭할 수 있으면 actor의 수대로 실행이 가능해서 attmpt 관리가 가능하다

def set_actor():
    return file.load_json("resources/2023-08-22/actors.json")

def set_object_extensions():
    list_ = []
    lecture_path = "resources/2023-08-22/task_not_scored/lecture"
    content_path = "resources/2023-08-22/task_not_scored/contents"
    listdir_ = [name for name in os.listdir(lecture_path) if 'task' in name]
    for lecture_name in listdir_:
        lecture = file.load_json(lecture_path+"/"+lecture_name)
        contents = file.load_json(content_path+"/"+lecture_name)
        list_.append([lecture, contents])
    
    return list_

class User(HttpUser):
    wait_time = between(1, 5)
    _actors = set_actor()
    _object_extensions = set_object_extensions()

    @task
    def task_1(self):
        session_id = str(uuid.uuid4())
        attempt = random.randint(1, 3)
        object_extensions = self._get_object_extensions()
        
        # origin_id = deepcopy(str(object_extensions[0]["object"]["definition"]["extensions"]["https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/id"]))
        # lecture_id = deepcopy(int(str(20000) + str(random.randint(1, 300))))
        # print(lecture_id)

        # object_extensions[0]["object"]["definition"]["extensions"]["https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/id"] = lecture_id
        # object_extensions[0]["object"]["id"] = object_extensions[0]["object"]["id"].replace(f"/lecture/{origin_id}", f"/lecture/{lecture_id}")

        # for contents in object_extensions[1]:
        #     contents["object"]["definition"]["extensions"]["https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/id"] = lecture_id
        #     contents["object"]["id"] = contents["object"]["id"].replace(f"/lecture/{origin_id}", f"/lecture/{lecture_id}")

        scenario = Cmi5Scenario(
            session_id=session_id,
            attempt=attempt,
            actor=self._get_actor(),
            lecture_object_context=object_extensions[0],
            contents_object_context=object_extensions[1]
        )
        is_assessed = "none"
        instructor_score = 0
        for full_statement, state in scenario.run_complted_with_contents():
            if state:
                if 'is_assessed' in state.get_body():
                    if state.get_body()["is_assessed"] == "false":
                        is_assessed = "false"
                    if state.get_body()["is_assessed"] == "true":
                        is_assessed = "true"
                    state.get_body()["is_assessed"] = is_assessed   

                    if "instructor_score" in state.get_body():
                        instructor_score = state.get_body()["instructor_score"]
                    
                    if instructor_score != 0:
                        state.get_body()["instructor_score"] = instructor_score

                self._state_api_request("POST", "/xAPI/activities/state", params=state.get_params(), body=state.get_body())
            # self._api_request("POST", "/xAPI/statements", full_statement)

    def on_start(self):
        """on_start is called when a Locust start before any task is scheduled"""
        self.client.verify = False

    def _get_actor(self):
        return self._actors[random.randint(1, 100) % len(self._actors)]["actor"]

    def _get_object_extensions(self):
        return self._object_extensions[random.randint(1, 100) % len(self._object_extensions)] 

    def _auth_header(self):
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Authorization": "Basic Og==",
            "X-Experience-API-Version": "1.0.3",
            "Accept": "*/*",
            "Host": "localhost:8000",
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
