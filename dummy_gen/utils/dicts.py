
def update_not_duplicated_key(dict1: dict, dict2: dict):
    origin_keys = dict1.keys()
    new_key = dict2.keys()

    for key in origin_keys:
        if key in new_key:
            raise KeyError
        
    dict1.update(dict2)
    return dict1
        

    


    

