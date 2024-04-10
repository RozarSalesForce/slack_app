def create_project_modal(client, body):
    client.views_open(
        trigger_id=body["trigger_id"],
        hash=body["view"]["hash"],
        view={
            "type": "modal",
            "callback_id": "create_project",
            "title": {
                "type": "plain_text",
                "text": "Enter Project details",
                "emoji": True,
            },
            "submit": {"type": "plain_text", "text": "Create", "emoji": True},
            "close": {"type": "plain_text", "text": "Cancel", "emoji": True},
            "blocks": [
                {
                    "block_id": "project_name",
                    "type": "input",
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "project_name",
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Project Name",
                        "emoji": True,
                    },
                },
                {
                    "block_id": "project_description",
                    "type": "input",
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "project_description",
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Description",
                        "emoji": True,
                    },
                },
                {
                    "block_id": "project_members",
                    "type": "input",
                    "element": {
                        "action_id": "project_members",
                        "type": "multi_users_select",
                        "placeholder": {"type": "plain_text", "text": "Select Members"},
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Select Members",
                        "emoji": True,
                    },
                },
            ],
        },
    )
