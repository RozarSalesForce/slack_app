from ..components.home.home_view import home_filter_view, home_view

def my_task(ack, body, logger, client, payload):
    try:
        ack()
        print(payload)
        user = body["user"]["id"]
        worspace = body["team"]["id"]
        if payload["value"] != "my_task":
            filter = {}
            filter["status"] = payload["value"]
            filter["assigneeUserName"] = user
            home_filter_view(client, user, filter, worspace)
        else:
            home_view(client, user, worspace)
        
    except Exception as e:
            logger.error(e)