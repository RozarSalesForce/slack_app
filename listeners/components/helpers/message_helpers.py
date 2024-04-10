def create_task_message(task, context):
    message = [
        {
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": f"Task is created",
				"emoji": True
			}
		},
        {
            "type": "rich_text",
            "block_id": "create_task_message",
            "elements": [
                {
                    "type": "rich_text_quote",
                    "elements": [
                        {
                            "type": "text",
                            "text": f" Id : {task["id"]} \nTitle : {task["title"]} \nDescription : {task["description"]} \nDue Date : {task["dueDate"]}",
                        },
                    ],
                }
            ],
        },
        {
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "See Details",
						"emoji": True
					},
					"value": "update_task",
					"action_id": f"update_task_{task["id"]}"
				}
			]
		}
    ]
    return message
