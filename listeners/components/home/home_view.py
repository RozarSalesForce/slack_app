from ...models.task import Task
from .home_actions import home_actions
from .home_login import home_login
from ...models.authHelpers import user_auth_check


def create_task_blocks(user_tasks):
    tasks = []
    for user_task in user_tasks:
        task = [
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"*{user_task['id']} - {user_task['title']} {" - " + user_task['status'] if "status" in user_task else ""}*"},
                "accessory":  {
                            "type": "button",
                            "text": {"type": "plain_text", "text": "Update", "emoji": True},
                            "value": "update_task",
                            "action_id": f"update_task_{user_task['id']}",
                            "style": "primary",
                        }
            },
            {
                "block_id": user_task['id'],
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"*{user_task['description']}*"},
                "accessory": {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Delete",
                                "emoji": True,
                            },
                            "value": "delete_task",
                            "action_id": f"delete_task_{user_task['id']}",
                            "style": "danger",
                        }
            },
            {"type": "divider"}
        ]
        tasks.extend(task)
    return tasks


def home_view(client, user, workspace):
    user_auth = user_auth_check(workspace, user)
    print(user_auth)
    if user_auth :
        data = {}
        data["filterValue"] = {"assigneeUserName": user}
        data["workspace"] = workspace
        data["user"] = user
        user_tasks = Task().findTask(data)
        if user_tasks:
            task_blocks = create_task_blocks(user_tasks)
            blocks = home_actions()
            blocks.extend(
                [
                    {
                        "type": "section",
                        "text": {
                            "type": "plain_text",
                            "text": "Tasks assigned to you are here",
                            "emoji": True,
                        },
                    },
                ]
            )
            blocks.extend(task_blocks)
            client.views_publish(user_id=user, view={"type": "home", "blocks": blocks})
        else:
            blocks = home_actions()
            client.views_publish(
                user_id=user,
                view={"type": "home", "callback_id": "home_view", "blocks": blocks},
            )
    else:
        blocks = home_login()
        client.views_publish(user_id=user, view={"type": "home", "blocks": blocks})


def home_filter_view(client, user, filter, workspace):
    data = {}
    data["filterValue"] = filter
    data["workspace"] = workspace
    data["user"] = user
    user_tasks = Task().findTask(data)
    blocks = home_actions()
    if user_tasks:
        task_blocks = create_task_blocks(user_tasks)
        blocks.extend(
            [
                {
                    "type": "section",
                    "text": {
                        "type": "plain_text",
                        "text": f"Filtered tasks {"for status " + filter["status"] if "status" in  filter else ""} ",
                        "emoji": True,
                    },
                },
            ]
        )
        blocks.extend(task_blocks)
        client.views_publish(user_id=user, view={"type": "home", "blocks": blocks})
    else:
        blocks.extend(
            [
                {"type": "divider"},
                {
                    "type": "section",
                    "text": {
                        "type": "plain_text",
                        "text": "No task found",
                        "emoji": True,
                    },
                },
            ]
        )
        client.views_publish(
            user_id=user,
            view={"type": "home", "callback_id": "home_view", "blocks": blocks},
        )
