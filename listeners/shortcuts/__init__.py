from slack_bolt import App

from .delete_created_task import delete_created_task

def register(app: App):
    app.shortcut("delete_created_task")(delete_created_task)