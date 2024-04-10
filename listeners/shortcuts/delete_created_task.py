from ..components.task.delete_task_modal import delete_task_modal

def delete_created_task(ack, body, logger, client):
    try:
        ack()
        task_id = "001"
        print(task_id)
        delete_task_modal(client, body, task_id)
    except Exception as e:
            logger.error(e)