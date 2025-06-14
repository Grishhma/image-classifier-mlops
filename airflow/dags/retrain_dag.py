from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'grishma',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='docker_retrain_classifier',
    default_args=default_args,
    description='Run Docker container to retrain image classifier',
    schedule_interval='@daily',  # or '@hourly', '0 9 * * *', etc.
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:
    
    retrain = BashOperator(
        task_id='run_docker_image_classifier',
        bash_command='docker run --rm -v /absolute/path/to/your/project:/app image-classifier'
    )
