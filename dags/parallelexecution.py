from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator


def clean_data():
    print("data is being getting cleaned")


with DAG(
    dag_id="mymondaydag1",
    start_date=datetime(2026, 9, 15),
    schedule="@daily",
    catchup=False,
) as dag:

    task1 = BashOperator(
        task_id="download_data",
        bash_command='echo "We are about to process data"',
    )

    task2 = PythonOperator(
        task_id="process_data",
        python_callable=clean_data,
    )

    task3=BashOperator(
        task_id="next_state_of_data",
        bash_command='echo "We are about to move to next stage"',
    )

    task1 >> [task2,task3]