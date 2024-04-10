from ..models.user import User
from ..models.authHelpers import store_jwt_token
from ..components.home.home_view import home_view

def register_user (view, ack, body, client, logger, context, say):
    try:
        ack()
        data = {}
        user_credentials = view["state"]["values"]
        print(user_credentials)
        data["workspace"] = view["team_id"]
        data["username"] = body["user"]["id"]
        data["password"] = user_credentials["password"]["password"]["value"]
        response = User().signup_user(data)
        print(response)

    except Exception as e:
        logger.error(e)

from ..models.user import User

def login_user (view, ack, body, client, logger, context, say):
    try:
        ack()
        data = {}
        user_credentials = view["state"]["values"]
        print(user_credentials)
        data["workspace"] = view["team_id"]
        data["username"] = body["user"]["id"]
        data["password"] = user_credentials["password"]["password"]["value"]
        response = User().login_user(data)
        print(response)
        if "salt" in response:
            store_jwt_token(data["workspace"], data["username"], response["salt"])
            print(response)
            home_view(client, data["username"], data["workspace"])
        else: 
            say(channel=data["username"], text="Wrong Password")

    except Exception as e:
        logger.error(e)