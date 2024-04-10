def home_actions():
    actions_block = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Welcome to Collaborative Task App !!",
            },
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Create Task",
                        "emoji": True,
                    },
                    "value": "create_task",
                    "action_id": "create_task",
                    "style": "primary",
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Join Project",
                        "emoji": True,
                    },
                    "value": "join_project",
                    "action_id": "join_project",
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Create Project",
                        "emoji": True,
                    },
                    "value": "create_project",
                    "action_id": "create_project",
                },
            ],
        },
        {"type": "divider"},
        {
            "type": "actions",
            "block_id": "search_task_buttons",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Search Tasks",
                        "emoji": True,
                    },
                    "value": "filter_task",
                    "action_id": "filter_task",
                }
            ],
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
                        "text": "My Tasks",
                        "emoji": True,
                    },
                    "value": "my_task",
                    "action_id": "my_task_all",
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "To Do",
                        "emoji": True,
                    },
                    "value": "Ready",
                    "action_id": "my_task_todo",
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "In Progress",
                        "emoji": True,
                    },
                    "value": "In Progress",
                    "action_id": "my_task_inprogress",
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Done",
                        "emoji": True,
                    },
                    "value": "Completed",
                    "action_id": "my_task_completed",
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "In QA",
                        "emoji": True,
                    },
                    "value": "In QA",
                    "action_id": "my_task_qa",
                },
            ],
        },
    ]
    return actions_block
