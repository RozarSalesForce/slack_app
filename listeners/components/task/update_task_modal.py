def update_task_modal(client, body, task):
    client.views_open(
        trigger_id=body["trigger_id"],
        view={
            "type": "modal",
            "callback_id": f"update_task_{task["id"]}",
            "title": {
                "type": "plain_text",
                "text": "Update task details",
                "emoji": True,
            },
            "submit": {"type": "plain_text", "text": "Update", "emoji": True},
            "close": {"type": "plain_text", "text": "Cancel", "emoji": True},
            "blocks": [
                {
                    "block_id": "title",
                    "type": "input",
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "title",
                        "initial_value": task["title"],
                    },
                    "label": {"type": "plain_text", "text": "Title", "emoji": True},
                },
                {
                    "block_id": "description",
                    "type": "input",
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "description",
                        "initial_value": task["description"],
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Description",
                        "emoji": True,
                    },
                },
                {
                    "block_id": "due_date",
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": "Pick a date for the deadline."},
                    "accessory": {
                        "type": "datepicker",
                        "initial_date": "1990-04-28",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Select a date",
                            "emoji": True,
                        },
                        "action_id": "due_date",
                        "initial_date": task["dueDate"],
                    },
                },
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
                                    "text": "Done",
                                    "emoji": True,
                                },
                                "value": "Completed",
                            },
                             {
                                "text": {
                                    "type": "plain_text",
                                    "text": "In QA",
                                    "emoji": True,
                                },
                                "value": "In QA",
                            }
                        ],
                        "action_id": "status",
                        "initial_option": {
                            "text": {
                                "type": "plain_text",
                                "text": task["status"],
                                "emoji": True
                            },
                            "value": task["status"],
                        },
                    },
                },
            ],
        },
    )
