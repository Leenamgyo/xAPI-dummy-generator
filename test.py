
import json
import os


def load_json(file_path):
    try:
        with open(file_path) as f:
            data = json.load(f)
        return data
    except FileNotFoundError as err:
        print(f"{err=}")
        raise FileNotFoundError
    

dir_path = "resources/2023-08-20"
lecture_path = "resources/2023-08-20/lecture"
content_path = "resources/2023-08-20/contents"


for lecture_name in os.listdir(lecture_path):
    lecture = load_json(lecture_path+"/"+lecture_name)
    contents = load_json(content_path+"/"+lecture_name)

    
    
