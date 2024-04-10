from ..components.home.home_view import home_filter_view

def find_all_tasks(view, ack, body, client, logger):
    try:
        ack()
        provided_values = view["state"]["values"]
        user = body["user"]["id"]
        workspace = body["team"]["id"]
        filterValue= {}
        print(provided_values)
        if provided_values["status"]["status"]["selected_option"]:
            filterValue["status"] = provided_values["status"]["status"]["selected_option"]["value"]
        filterValue["assigneeUserName"] = provided_values["assignee_user_id"]["assignee_user_id"]["selected_user"]
        print(filterValue)
        home_filter_view(client, user, filterValue, workspace)

    except Exception as e:
        logger.error(e)