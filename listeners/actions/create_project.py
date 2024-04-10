from ..components.project.create_project_modal import create_project_modal

def create_project(ack, body, logger, client):
    try:
        ack()
        create_project_modal(client, body)
        
    except Exception as e:
            logger.error(e)