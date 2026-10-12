from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id="addopeartor",
    start_date=datetime(2026, 9, 15),
    schedule="@daily",
    catchup=False,
) as dag:

    task1 = BashOperator(
        task_id="download_data",
        bash_command="mkdir -p ~/airflow/dags/dushera && echo 'dushera folder created'",
    )