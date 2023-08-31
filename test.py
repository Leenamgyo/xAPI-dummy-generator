import time
import uuid
import random
import os 

from xapi_app.scenario import Cmi5Scenario
from xapi_app.utils import file


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

def _get_actor(index=None):
    if not index:
        index = random.randint(1, 100) % len(_actors)
    
    return _actors[index % len(_actors)]["actor"], index

def _get_object_extensions():
    return _object_extensions[random.randint(1, 100) % len(_object_extensions)] 

session_id = str(uuid.uuid4())
attempt = random.randint(1, 3)
object_extensions = _get_object_extensions()
actor, rand_index = _get_actor()
index = 0
scenario = Cmi5Scenario(
    session_id=session_id,
    attempt=attempt,
    actor=actor,
    lecture_object_context=object_extensions[0],
    contents_object_context=object_extensions[1]
)

for full_statement, state in scenario.run_peer_submit():
    index = index + 1
    file.store_json(f"full_statement{index}.json", full_statement)

    if state:
        state_json = [state.get_params(), state.get_body()]
        file.store_json(f"state{index}.json", state_json)

evaluation_id = int(scenario.contents[0]['object']['id'][scenario.contents[0]['object']['id'].rindex("/")+1:] + str(rand_index).rjust(2,"0"))
for full_statement, state in scenario.run_peer_review(actor, evaluation_id, 'self'):
    index = index + 1
    file.store_json(f"full_statement_reviewer_01{index}.json", full_statement)

    if state:
        state_json = [state.get_params(), state.get_body()]
        file.store_json(f"state{index}.json", state_json)

for full_statement, state in scenario.run_peer_review(_get_actor(rand_index+5)[0], evaluation_id, "peer"):
    index = index + 1
    file.store_json(f"full_statement_reviewer_02{index}.json", full_statement)

    if state:
        state_json = [state.get_params(), state.get_body()]
        file.store_json(f"state{index}.json", state_json)


for full_statement, state in scenario.run_peer_review(_get_actor(rand_index+10)[0], evaluation_id, "peer"):
    index = index + 1
    file.store_json(f"full_statement_reviewer_03{index}.json", full_statement)

    if state:
        state_json = [state.get_params(), state.get_body()]
        file.store_json(f"state{index}.json", state_json)


for full_statement, state in scenario.run_peer_scored():
    index = index + 1
    file.store_json(f"full_statement_reviewer_04{index}.json", full_statement)
    
    if state:
        state_json = [state.get_params(), state.get_body()]
        file.store_json(f"state{index}.json", state_json)

    
