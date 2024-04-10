from ..components.authentication.register_user_modal import register_user_modal
from ..components.authentication.login_user_modal import login_user_modal

def register_user(ack, body, logger, client):
    try:
        ack()
        user = body["user"]["id"]
        print(user)
        register_user_modal(client, body)
        
    except Exception as e:
            logger.error(e)

def login_user(ack, body, logger, client):
    try:
        ack()
        user = body["user"]["id"]
        print(user)
        login_user_modal(client, body)
        
    except Exception as e:
            logger.error(e)