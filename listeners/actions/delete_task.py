from ..components.task.delete_task_modal import delete_task_modal

def delete_task(ack, body, logger, client, payload):
    try:
        ack()
        task_id = payload['action_id'].replace('delete_task_', '')
        delete_task_modal(client, body, task_id)  
        
    except Exception as e:
            logger.error(e)