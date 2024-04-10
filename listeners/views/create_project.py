from ..models.project import Project

def create_project (view, ack, body, client, logger, context, say):
    try:
        ack()
        data = view["state"]["values"]
        project = {}

        project["name"] = data["project_name"]["project_name"]["value"]
        project["workspace"] = body["team"]["id"]
        project["user"] = body["user"]["id"]
        project["description"] = data["project_description"]["project_description"]["value"]
        project["members"] = data["project_members"]["project_members"]["selected_users"]
        channel_name = project["name"].replace(' ', '-')
        Project().createProject(project)
        channel = client.conversations_create(
            name=channel_name,
            is_private=True
        )
        if not channel["ok"]:
            say(channel=body["user"]["id"], text="you don't have permission to create project")
        channel = channel["channel"]
        client.conversations_invite(
            channel=channel["id"],
            users=project["members"]
        )
        say(channel=body["user"]["id"], text="Project is created")

    except Exception as e:
        logger.error(e)