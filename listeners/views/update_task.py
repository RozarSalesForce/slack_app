from ..components.home.home_view import home_view
from ..models.task import Task

def update_task(view, ack, body, say, client, logger, payload):
    try:
        ack()
        task_data = view["state"]["values"]
        print(task_data)
        user = body["user"]["id"]
        workspace = body["team"]["id"]
        task_id = payload['callback_id'].replace('update_task_', '')
        data = {}
        data["user"] = user
        data["workspace"] = workspace
        data["id"] = str(task_id)
        data["title"] = task_data["title"]["title"]["value"]
        data["description"] = task_data["description"]["description"]["value"]
        data["assigneeUserName"] = user
        data["status"] = task_data["status"]["status"]["selected_option"]["value"]
        data["dueDate"] = task_data["due_date"]["due_date"]["selected_date"]
        Task().updateTask(data)
        say(channel=user,text=f"{task_id} task is updated")
        if user != data["assigneeUserName"]:
            say(channel=data["assigneeUserName"],text=f"{task_id} task is updated and assigned to you")
        home_view(client, user, body["team"]["id"])

    except Exception as e:
        logger.error(e)