def login_user_modal(client, body):
    client.views_open(
        trigger_id=body["trigger_id"],
        view={
            "type": "modal",
            "callback_id": "login_user", 
            "title": {
                "type": "plain_text",
                "text": "Enter Password",
                "emoji": True,
            },
            "submit": {"type": "plain_text", "text": "Login", "emoji": True},
            "close": {"type": "plain_text", "text": "Cancel", "emoji": True},
            "blocks": [
                {
                    "block_id": "user_id",
                    "type": "context",
                    "elements": [
                        {"type": "mrkdwn", "text": f"{body["user"]["id"]}"},
                    ],
                },
                {
                    "block_id": "password",
                    "type": "input",
                    "element": {"type": "plain_text_input", "action_id": "password"},
                    "label": {"type": "plain_text", "text": "Password", "emoji": True},
                },
            ],
        },
    )
