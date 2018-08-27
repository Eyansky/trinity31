"""Database structure 
"""

USERS_LIST = []

def add_user(username, password):
    user_id = 1
    if len(USERS_LIST) > 0:
        user_id = USERS_LIST[-1]["id"] + 1
    new_user = {
        "id": user_id,
        "username": username,
        "password": password,
        "role": "user"
    }

    USERS_LIST.append(new_user)
    return True


