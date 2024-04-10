from listeners import actions
from listeners import events
from listeners import views
from listeners import shortcuts

def register_listeners(app):
    actions.register(app)
    events.register(app)
    views.register(app)
    shortcuts.register(app)