import json

def store_json(file_path, data):
    try:
        with open(file_path, "w") as outfile:
            json.dump(data, outfile, indent=4)
        return data
    except FileNotFoundError as err:
        print(f"{err=}")
        raise FileNotFoundError
    
    
def load_json(file_path):
    try:
        with open(file_path) as f:
            data = json.load(f)
        return data
    except FileNotFoundError as err:
        print(f"{err=}")
        raise FileNotFoundError