import random
from ..components.home.home_view import home_view
from ..models.task import Task
from ..components.helpers.message_helpers import create_task_message

def create_new_task(view, ack, body, client, logger, context, say):
    try:
        ack()
        task_data = view["state"]["values"]
        user = body["user"]["id"]
        data = {}
        task_id = random.randint(1000, 9999)
        data["workspace"] = view["team_id"]
        data["id"] = str(task_id)
        data["title"] = task_data["title"]["title"]["value"]
        data["description"] = task_data["description"]["description"]["value"]
        data["assigneeUserName"] = user
        data["status"] = task_data["status"]["status"]["selected_option"]["value"]
        data["dueDate"] = task_data["due_date"]["due_date"]["selected_date"]

        Task().createTask(data)
        
        say(
            channel=data["assigneeUserName"],
            blocks=create_task_message(data, context),
            text = "hello"
        )
        home_view(client, user, body["team"]["id"])

    except Exception as e:
        logger.error(e)