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
        # NOTE: string.template 과 nested 항목에 대해서 호환이 잘 안맞음. 
        # "key": "value" 이런식으로 String을 감싸는 방식이 double quote가 나와야 json.load시 오류가 걸리지 않는다. 
        # 그러나, template으로 load 시키는 방법은 \'key\' = \'value\' 이런 식으로 나오기 때문에 json.load시 오류가 발생한다. 
        # 거기에 대한 임시적인 방안으로 다음과 같이 작성하였다. 

        if isinstance(v, dict):
            kwargs[k] = json.dumps(v)
        elif isinstance(v, list):
            if isinstance(v[0], dict):
                kwargs[k] = json.dumps(v)
            else:
                kwargs[k] = json.dumps(v)
            # for idx, x in enumerate(v):
            #     if isinstance(x, dict):
            #         kwargs[k][idx] = json.dumps(x)

    template = load_template(file_path)
    return template.substitute(kwargs)
    

