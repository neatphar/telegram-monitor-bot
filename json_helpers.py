import json

def retrieve_db(key):
    """
    Retrieves a value from the json file based on the key input.
    
    Parameters:
        key (str): The key of the value required.
        
    Returns:
        Object
    """
    data = json.load(open('data.json'))
    if key not in data.keys():
        return None
    return data[key]

def set_db(key, val):
    """
    Sets a value in the json file based on the key input.
    
    Parameters:
        key (str): The key of the value required.
        val (obj): the new value of that key.
    Returns:
        Object
    """
    db = json.load(open('data.json'))
    db[key] = val
    return json.dump(db, open('data.json', 'w'))

