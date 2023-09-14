import time
import uuid
import random
import os 

from xapi_app.scenario import Cmi5Scenario
from xapi_app.utils import file



def set_actor():
    return file.load_json("resources/actors.json")

def set_object_extensions():
    list_ = []
    lecture_path = "resources/quiz/lecture"
    content_path = "resources/quiz/contents"
    for lecture_name in os.listdir(lecture_path):
        lecture = file.load_json(lecture_path+"/"+lecture_name)
        contents = file.load_json(content_path+"/"+lecture_name)
        list_.append([lecture, contents])
    
    return list_

_actors = set_actor()
_object_extensions = set_object_extensions()

def _get_actor():
    return _actors[random.randint(1, 100) % len(_actors)]["actor"]

def _get_object_extensions():
    return _object_extensions[random.randint(1, 100) % len(_object_extensions)] 

session_id = str(uuid.uuid4())
attempt = random.randint(1, 3)
object_extensions = _get_object_extensions()

scenario = Cmi5Scenario(
    session_id=session_id,
    attempt=attempt,
    actor=_get_actor(),
    lecture_object_context=object_extensions[0],
    contents_object_context=object_extensions[1]
)
index = 0
instructor_score = 0
for full_statement, state in scenario.run_complted_with_contents():
    index = index + 1
    file.store_json(f"full_statement{index}.json", full_statement)
    
    if state:
        state_json = [state.get_params(), state.get_body()]
        file.store_json(f"state{index}.json", state_json)
