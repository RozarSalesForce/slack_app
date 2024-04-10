from ..components.task.create_task_modal import create_task_modal

def create_task(ack, body, logger, client):
    try:
        ack()
        create_task_modal(client, body)
        
    except Exception as e:
            logger.error(e)