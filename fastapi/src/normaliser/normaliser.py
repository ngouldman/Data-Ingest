import json


class DataValidationErrors(Exception):

    pass

def normalise(data: dict) -> dict:
    
    schema = {"name"}

    for field in schema:
        data.get(field, None)
    
    name = data.get("name", None)

    if not name:
        raise DataValidationErrors(f'missing required field: name, instead found {data}')
    else:
        print("validation passed")

def convert(data):
    
    json.loads(data)

    return data


normalise()