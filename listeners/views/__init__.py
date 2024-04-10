import re
from slack_bolt import App

from .create_new_task import create_new_task
from .delete_task import delete_task
from .find_all_tasks import find_all_tasks
from .update_task import update_task
from .authentication import register_user, login_user
from .create_project import create_project

def register(app: App):
    app.view("create_new_task")(create_new_task)
    app.view(re.compile("delete_task_(.+)"))(delete_task)
    app.view("find_all_tasks")(find_all_tasks)
    app.view(re.compile("update_task_(.+)"))(update_task)
    app.view("register_user")(register_user)
    app.view("login_user")(login_user)
    app.view("create_project")(create_project)