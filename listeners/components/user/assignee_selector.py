def assignee_selector():
    block = [
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
        }
    ]
    return block
