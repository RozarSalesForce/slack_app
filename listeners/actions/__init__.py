import re
from slack_bolt import App

from .create_task import create_task
from .delete_task import delete_task
from .filter_task import filter_task
from .my_tasks import my_task
from .update_task import update_task
from .authentication import register_user, login_user
from .create_project import create_project
def register(app: App):
    app.action("create_task")(create_task)
    app.action(re.compile("delete_task_(.+)"))(delete_task)
    app.action("filter_task")(filter_task)
    app.action(re.compile("my_task_(.+)"))(my_task)
    app.action(re.compile("update_task_(.+)"))(update_task)
    app.action("register_user")(register_user)
    app.action("login_user")(login_user)
    app.action("create_project")(create_project)