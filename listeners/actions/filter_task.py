from ..components.task.find_task_modal import find_task_modal

def filter_task(ack, body, logger, client):
    try:
        ack()
        find_task_modal(client, body)
        
    except Exception as e:
            logger.error(e)