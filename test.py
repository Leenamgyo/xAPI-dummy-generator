import time
import uuid
import random
import os 
import requests

from xapi_app.scenario import Cmi5Scenario
from xapi_app.utils import file
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def _auth_header():
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "Basic Og==",
        "X-Experience-API-Version": "1.0.3",
        "Accept": "*/*",
        "Host": "cne-lrs.bubblecon.io",
    }
    return headers

def _api_request(url, body=None):
    return requests.post(
        url=url,
        verify=False,
        json=body,
        headers=_auth_header(),
    )

def _state_api_request(url, body=None, params=None):
    return requests.post(
        url,
        verify=False,
        json=body,
        headers=_auth_header(),
        params=params,
    )

def _response_check(response):
    if not (response.status_code == 200 or response.status_code == 204):
        print("error")

def set_actor():
    return file.load_json("resources/peer/actors.json")

def set_object_extensions():
    list_ = []
    lecture_path = "resources/peer/lecture"
    content_path = "resources/peer/contents"
    for lecture_name in os.listdir(lecture_path):
        lecture = file.load_json(lecture_path+"/"+lecture_name)
        contents = file.load_json(content_path+"/"+lecture_name)
        list_.append([lecture, contents])
    
    return list_

_actors = set_actor()
_object_extensions = set_object_extensions()

def _get_actor(index_):
    return _actors[index_ % len(_actors)]["actor"], index_

def _get_object_extensions(index_):
    return _object_extensions[index_ % len(_object_extensions)] 

for ob_ext_index in range(len(_object_extensions)):
    for index, _ in enumerate(_actors):
        print(f"{ob_ext_index=}")
        print(f"{index=}")
        session_id = str(uuid.uuid4())
        attempt = random.randint(1, 3)
        object_extensions = _get_object_extensions(ob_ext_index)
        actor, rand_index = _get_actor(index)
        index = 0
        scenario = Cmi5Scenario(
            session_id=session_id,
            attempt=attempt,
            actor=actor,
            lecture_object_context=object_extensions[0],
            contents_object_context=object_extensions[1]
        )
        
        subimit_id = int(scenario.contents[0]['object']['id'][scenario.contents[0]['object']['id'].rindex("/")+1:] + str(rand_index).rjust(2,"0"))
        print(f"submit_id: {subimit_id}")
        for full_statement, state in scenario.run_peer_submit(subimit_id):
            index = index + 1
            # file.store_json(f"full_statement_submit_{index}.json", full_statement)   
            _response_check(_api_request("https://cne-lrs.bubblecon.io/xAPI/statements", full_statement))

            if state:
                state_json = [state.get_params(), state.get_body()]
                # file.store_json(f"state{index}.json", state_json)
                _response_check(_state_api_request("https://cne-lrs.bubblecon.io/xAPI/activities/state", body=state.get_body(), params=state.get_params()))

        review_1_id = int(str(subimit_id) + str(rand_index).rjust(2,"0"))
        for full_statement, state in scenario.run_peer_review(actor, subimit_id, review_1_id, 'self'):
            index = index + 1
            # file.store_json(f"full_statement_reviewer_01{index}.json", full_statement)
            _response_check(_api_request("https://cne-lrs.bubblecon.io/xAPI/statements", full_statement))

            if state:
                state_json = [state.get_params(), state.get_body()]
                # file.store_json(f"state{index}.json", state_json)
                _response_check(_state_api_request("https://cne-lrs.bubblecon.io/xAPI/activities/state", body=state.get_body(), params=state.get_params()))

        review_2_id = int(str(subimit_id) + str(rand_index + 5).rjust(2,"0"))
        for full_statement, state in scenario.run_peer_review(_get_actor(rand_index+5)[0], subimit_id, review_2_id, "peer"):
            index = index + 1
            # file.store_json(f"full_statement_reviewer_02{index}.json", full_statement)
            _response_check(_api_request("https://cne-lrs.bubblecon.io/xAPI/statements", full_statement))

            if state:
                state_json = [state.get_params(), state.get_body()]
                # file.store_json(f"state{index}.json", state_json)
                _response_check(_state_api_request("https://cne-lrs.bubblecon.io/xAPI/activities/state", body=state.get_body(), params=state.get_params()))


        review_3_id = int(str(subimit_id) + str(rand_index + 10).rjust(2,"0"))
        for full_statement, state in scenario.run_peer_review(_get_actor(rand_index+10)[0], subimit_id, review_3_id, "peer"):
            index = index + 1
            # file.store_json(f"full_statement_reviewer_03{index}.json", full_statement)
            _response_check(_api_request("https://cne-lrs.bubblecon.io/xAPI/statements", full_statement))

            if state:
                state_json = [state.get_params(), state.get_body()]
                # file.store_json(f"state{index}.json", state_json)
                _response_check(_state_api_request("https://cne-lrs.bubblecon.io/xAPI/activities/state", body=state.get_body(), params=state.get_params()))


        for full_statement, state in scenario.run_peer_scored(subimit_id):
            index = index + 1
            # file.store_json(f"full_statement_reviewer_04{index}.json", full_statement)
            _response_check(_api_request("https://cne-lrs.bubblecon.io/xAPI/statements", full_statement))
            
            if state:
                state_json = [state.get_params(), state.get_body()]
                # file.store_json(f"state{index}.json", state_json)
                _response_check(_state_api_request("https://cne-lrs.bubblecon.io/xAPI/activities/state", body=state.get_body(), params=state.get_params()))

    
