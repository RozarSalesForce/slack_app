from slack_bolt import App

from .app_home_opened import update_home_tab

def register (app: App):
    app.event("app_home_opened")(update_home_tab)