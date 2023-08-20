import json
import string

def store_json(file_path, data):
    try:
        with open(file_path, "w") as outfile:
            json.dump(data, outfile, indent=4)
        return data
    except FileNotFoundError as err:
        print(f"{err=}")
        raise FileNotFoundError
    

def load_json_file(file_path) -> dict:
    try:
        with open(file_path) as f:
            data = json.load(f)
            return data
    except FileNotFoundError as err:
        print(f"{err=}")
        raise FileNotFoundError

def load_template(file_path):
    with open(file_path, 'r') as f:
        src = string.Template(f.read())
    return src

def load_template_subs(file_path, **kwargs):
    for k, v in kwargs.items():
        if isinstance(v, dict):
            kwargs[k] = json.dumps(v)
        elif isinstance(v, list):
            if isinstance(v[0], dict):
                kwargs[k] = json.dumps(v)
            else:
                kwargs[k] = str(v)
            # for idx, x in enumerate(v):
            #     if isinstance(x, dict):
            #         kwargs[k][idx] = json.dumps(x)

    template = load_template(file_path)
    return template.substitute(kwargs)
    

