def find_task_modal(client, body):
    client.views_open(
        trigger_id=body["trigger_id"],
        view={
            "type": "modal",
            "callback_id": "find_all_tasks",
            "title": {
                "type": "plain_text",
                "text": "Enter Filter details",
                "emoji": True,
            },
            "submit": {"type": "plain_text", "text": "Find", "emoji": True},
            "close": {"type": "plain_text", "text": "Cancel", "emoji": True},
            "blocks": [
                {
                    "block_id": "status",
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": "Select task status"},
                    "accessory": {
                        "type": "static_select",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Select an item",
                            "emoji": True,
                        },
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Ready",
                                    "emoji": True,
                                },
                                "value": "Ready",
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "In Progress",
                                    "emoji": True,
                                },
                                "value": "In Progress",
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Completed",
                                    "emoji": True,
                                },
                                "value": "value-2",
                            },
                        ],
                        "action_id": "status"
                    },
                },
                {
                    "block_id": "assignee_user_id",
                    "type": "input",
                    "element": {
                        "type": "users_select",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Assignee",
                        },
                        "action_id": "assignee_user_id",
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Assignee Username",
                        "emoji": True,
                    }
                },
            ],
        },
    )
