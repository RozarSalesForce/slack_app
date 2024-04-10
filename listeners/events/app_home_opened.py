from ..components.home.home_view import home_view

def update_home_tab(body, logger, client, event):
  try:
    user = event['user']
    print(user)
    home_view(client, user, body["team_id"])
  except Exception as e:
    logger.error(f"Error publishing home tab: {e}")