import os
import json
from datetime import date
import random
import utils
from copy import deepcopy
import urllib3

OBJECT_ID_PREFIX = "https://class.whalespace.io/bubblecon-guide/lecture"
DIR_PATH = f"dummy_gen/{str(date.today())}"

def find_contents(lecture):
    contents = utils.files.load_json_file(f"dummy_gen/whaleclass/{lecture['lecture_type']}_contents.json")
    selected = random.sample(contents, 10)

    if lecture['lecture_type'] == "peer":
        contents = utils.files.load_json_file(f"dummy_gen/whaleclass/{lecture['lecture_type']}_contents.json")
        selected = random.sample(contents, 1)

    return selected


def extra_content_data(content_info, object_extensions):
    return object_extensions

def extra_data(lecture_info, object_extensions):
    if lecture_info["lecture_type"] == "quiz":
        object_extensions["https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/quiz-type"] = lecture_info["lecture_quiz_type"]
    elif lecture_info["lecture_type"] == "task":
        pass
    elif lecture_info["lecture_type"] == "peer":
        object_extensions["https://class.whalespace.io/classes/class/chapters/chapter/lectures/peer/assessment/start-date"] = lecture_info["assessment_start_date"]
        object_extensions["https://class.whalespace.io/classes/class/chapters/chapter/lectures/peer/assessment/end-date"] = lecture_info["assessment_end_date"]
        object_extensions["https://class.whalespace.io/classes/class/chapters/chapter/lectures/peer/assessment/number"] = lecture_info["assessment_number"]
    return object_extensions

def main():
    # actors = file.load_json("../resources/actors.json")
    class_info = utils.files.load_json_file("dummy_gen/whaleclass/class.json")
    lecture_infos: list[dict] = utils.files.load_json_file("dummy_gen/whaleclass/cmi5.json")
    context_info: dict = utils.files.load_json_file("dummy_gen/whaleclass/context.json")

    result_lecture_contents = list()
    for lecture_info in lecture_infos:

        lecture_info = utils.dicts.update_not_duplicated_key(lecture_info, class_info)
        lecture_info["object_id"] = f"{OBJECT_ID_PREFIX}/{lecture_info['lecture_id']}"
        lecture_info["object_name"] = lecture_info["lecture_name"]
        lecture_info["object_description"] = lecture_info["lecture_name"]
        
        object_definition_extensions: str = utils.files.load_template_subs("dummy_gen/template/whaleclass_cmi5_object_extensions.template", **lecture_info)
        object_definition_extensions: dict = json.loads(object_definition_extensions) 
        object_definition_extensions = extra_data(lecture_info, object_definition_extensions)
        lecture_info["object_extensions"] = object_definition_extensions

        context_extensions: str = utils.files.load_template_subs("dummy_gen/template/whaleclass_cmi5_context_extensions.template", **lecture_info)
        context_extensions: dict = json.loads(context_extensions)
        lecture_context = deepcopy(context_info)
        lecture_context["extensions"] = context_extensions

        xapi_object = utils.files.load_template_subs("dummy_gen/template/default_object.template", **lecture_info)   
        xapi_object: dict = json.loads(xapi_object)

        xapi_context = utils.files.load_template_subs("dummy_gen/template/context.template", **lecture_context)   
        xapi_context: dict = json.loads(xapi_context)
        result_lecture = dict({"object":xapi_object, "context": xapi_context})
        
        content_infos = find_contents(lecture_info)
        result_contents = []
        for index, content_info in enumerate(content_infos):
            content_object_extensions = None
            xapi_content_object = None
            xapi_content_context = None

            content_info["content_order"] = index+1
            content_info["content_id"] = int(f"{lecture_info['lecture_id']}{random.randint(1, 3000)}")
            
            content_object_extensions = utils.files.load_template_subs("dummy_gen/template/whaleclass_content_object_extensions.template", **content_info)
            content_object_extensions: dict = json.loads(content_object_extensions)
            content_object_extensions = utils.dicts.update_not_duplicated_key(content_object_extensions, object_definition_extensions)
            content_object_extensions = extra_content_data(content_info, content_object_extensions)

            content_info["object_id"] = lecture_info["object_id"] + "/contents/" + str(content_info["content_id"])
            content_info["object_name"] = content_info["content_name"]
            content_info["object_description"] = content_info["content_description"]
            content_info["object_extensions"] = content_object_extensions

            if "interactionType" in content_info and content_info["interactionType"] == "choice":
                xapi_content_object = utils.files.load_template_subs("dummy_gen/template/choice_object.template", **content_info)
            elif "interactionType" in content_info and content_info["interactionType"] == "fill-in":
                xapi_content_object = utils.files.load_template_subs("dummy_gen/template/fill_in_object.template", **content_info)
            elif "interactionType" in content_info and content_info["interactionType"] == "long-fill-in":
                xapi_content_object = utils.files.load_template_subs("dummy_gen/template/long_fill_in_object.template", **content_info)
            else:
                xapi_content_object = utils.files.load_template_subs("dummy_gen/template/default_object.template", **content_info)
            xapi_content_object : dict = json.loads(xapi_content_object)

            xapi_content_context = utils.files.load_template_subs("dummy_gen/template/context.template", **context_info)   
            xapi_content_context: dict = json.loads(xapi_content_context)
            result_contents.append({"object": xapi_content_object, "context": xapi_content_context})

        result_lecture_contents.append([lecture_info, result_lecture,result_contents])
        

    lecture_dirpath = os.path.join(DIR_PATH, "lecture")
    contents_dirpath = os.path.join(DIR_PATH, "contents")

    os.makedirs(DIR_PATH, exist_ok=True)    
    os.makedirs(lecture_dirpath, exist_ok=True)
    os.makedirs(contents_dirpath, exist_ok=True)
    for index, result in enumerate(result_lecture_contents):
        file_name = f"{result[0]['lecture_type']}_{result[0]['lecture_id']}.json"
        utils.files.store_json(os.path.join(lecture_dirpath, file_name), result[1])
        
        file_name = f"{result[0]['lecture_type']}_{result[0]['lecture_id']}.json"
        utils.files.store_json(os.path.join(contents_dirpath, file_name), result[2])




if __name__ == "__main__":
    main()