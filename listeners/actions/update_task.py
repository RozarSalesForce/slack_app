from ..components.task.update_task_modal import update_task_modal
from ..models.task import Task
from ..models.authHelpers import user_auth_check

def update_task(ack, body, logger, client, payload, say):
    try:
        ack()
        task_id = payload['action_id'].replace('update_task_', '')
        user = body["user"]["id"]
        data = {}
        data["workspace"] = body["team"]["id"]
        data["user"] = user
        data["taskId"] = task_id
        task = Task().getTask(data)[0]
        if user_auth_check(body["team"]["id"],user) == False:
            say(channel=user, text="You are not authorized, Please login first from home tab !!")
            return
        update_task_modal(client, body, task)
        
    except Exception as e:
            logger.error(e)