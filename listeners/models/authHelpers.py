from .mongo import db

def fetch_jwt_token(workspace, user):
    key = f"{workspace}:{user}"
    result = db.jwt.find_one({"key": key})
    print(result)
    if result : 
        return result["jwt"]
    return False


def store_jwt_token(workspace, user, jwt):
    print(jwt)
    key = f"{workspace}:{user}"
    data = {"key": key, "jwt": jwt}
    db.jwt.insert_one(data)


def user_auth_check(workspace, user):
    if fetch_jwt_token(workspace, user):
        return True
    return False
