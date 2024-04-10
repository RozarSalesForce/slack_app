import os
# Use the package we installed
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from listeners import register_listeners

# Initialize your app with your bot token and signing secret
# app = App(
#     token=os.environ.get("SLACK_BOT_TOKEN"),
#     signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
# )

# Initialize your app with socket connection
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))
register_listeners(app)

def main():
   handler = SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN"))
   handler.start()

# Ready? Start your app!
if __name__ == "__main__":
    # app.start(port=int(os.environ.get("PORT", 3000)))
   main()
