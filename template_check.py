from json_helpers import retrieve_db, set_db
import requests



if retrieve_db('user_status') is None:
    set_db('user_status', "active")


def template_tick():
    """
    This template function is to check if a specific user status changed using a public API.
    
    Parameters:
        None
        
    Returns:
        Dictionary: {
            update (bool): whether to notify the users or not.
            message (str): the update message.
        }
    """
    response = requests.get('https://gorest.co.in/public/v2/users/3584').json()
    ret = {"update": False, "message": ""}
    if response.text != retrieve_db('user_status'):
        ret["update"] = True
        ret["message"] = f"The user {response['name']}'s status changed and is now {response['status']}."
        set_db('user_status', response["status"])
    return ret
