from ..models.task import Task
from ..components.home.home_view import home_view

def delete_task(ack, body, say, logger, payload, client):
    try:
        ack()
        task_id = payload['callback_id'].replace('delete_task_', '')
        user = body["user"]["id"]
        print(task_id)
        response = Task().deleteTask(task_id)
        say(channel=user,text=f"{task_id + " " + response["message"]}")
        home_view(client, user, body["team"]["id"])

    except Exception as e:
        logger.error(e)