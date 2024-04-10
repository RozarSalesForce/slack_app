def task_status_selector():
    block = [
        {
            "block_id": "status",
            "type": "section",
            "element": {
                "type": "static_select",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Select Task Status",
                    "emoji": True,
                },
                "options": [
                    {
                        "text": {"type": "plain_text", "text": "Ready", "emoji": True},
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
                        "value": "Completed",
                    },
                ],
                "label": {
                    "type": "plain_text",
                    "text": "Task Status",
                    "emoji": True,
                },
                "action_id": "status",
            },
        }
    ]
    return block
