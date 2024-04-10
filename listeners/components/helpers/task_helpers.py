def status_selector(task):
    return (
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
                "initial_value": task["status"],
                "action_id": f"change_status_{task["id"]}",
            },
        },
    )


def assignee_selector(task):
    return (
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
            },
            "initial_value": task["assigneeUserName"],
            "action_id": f"change_assignee_{task["id"]}"
        },
    )
