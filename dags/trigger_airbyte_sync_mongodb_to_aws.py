from datetime import datetime, timedelta
from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator


AIRBYTE_CONN_ID = 'airbyte_default'
TRIGGER_AIRBYTE_SYNC_MONGODB_AWS_ID = 'cfdd275b-791d-4f57-acb7-b1b5cc694301'

default_args = {
    'owner': 'bruno.almeida',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}


@dag(
    dag_id='trigger_airbyte_sync_mongodb_to_aws',
    start_date=datetime(year=2025, month=2, day=15),
    max_active_runs=1,
    schedule='@daily',
    catchup=False,
    default_args=default_args,
    owner_links={
        'LinkedIn': 'https://www.linkedin.com/in/brunohalmeida-contato/'
    },
    tags=['development', 'airbyte', 'mongodb', 'aws']
)
def trigger_airbyte_sync_mongodb_to_aws_dag():
    '''
    ## DAG: Trigger Airbyte Sync MongoDB to AWS
    
    This DAG is responsible for triggering an Airbyte synchronization process 
    between MongoDB and AWS. The process ensures data is consistently transferred 
    from the source database to the destination on AWS.
    
    ### Tasks:
    - **start_task**: Marks the beginning of the workflow.
    - **trigger_airbyte_sync_mongodb_to_aws_task**: Calls Airbyte to sync data.
    - **end_task**: Marks the end of the workflow.
    '''

    start_task = EmptyOperator(task_id='start_task')
    end_task = EmptyOperator(task_id='end_task')

    trigger_airbyte_sync_mongodb_to_aws_task = AirbyteTriggerSyncOperator(
        task_id='trigger_airbyte_sync_mongodb_to_aws_task',
        connection_id=TRIGGER_AIRBYTE_SYNC_MONGODB_AWS_ID,
        airbyte_conn_id=AIRBYTE_CONN_ID,
        asynchronous=False,
        timeout=3600,
        wait_seconds=3
    )

    start_task >> trigger_airbyte_sync_mongodb_to_aws_task >> end_task


trigger_airbyte_sync_mongodb_to_aws_dag()
