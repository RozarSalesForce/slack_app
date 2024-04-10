def home_login():
    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Welcome to Collaborative Task App !!",
            },
        },
        {
			"type": "context",
			"elements": [
				{
					"type": "plain_text",
					"text": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum",
					"emoji": True
				}
			]
		},
        {"type": "divider"},
        {
            "type": "actions",
            "block_id": "task_buttons",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Login",
                        "emoji": True,
                    },
                    "value": "login",
                    "action_id": "login_user",
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Register",
                        "emoji": True,
                    },
                    "value": "register",
                    "action_id": "register_user",
                }
            ],
        },
    ]
    return blocks
