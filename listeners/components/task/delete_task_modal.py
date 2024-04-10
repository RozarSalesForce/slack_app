def delete_task_modal(client, body, task_id):
    client.views_open(
        trigger_id=body["trigger_id"],
        view={
            "type": "modal",
            "callback_id": f"delete_task_{task_id}",
            "title": {
                "type": "plain_text",
                "text": "Enter task details",
                "emoji": True,
            },
            "submit": {"type": "plain_text", "text": "Confirm", "emoji": True},
            "close": {"type": "plain_text", "text": "Cancel", "emoji": True},
            "blocks": [
                {
                    "block_id": "task_id",
                    "type": "context",
                    "elements": [
                        {"type": "mrkdwn", "text": f"Please confirm you want to delte task - *{task_id}*"},
                    ],
                }
            ],
        },
    )
