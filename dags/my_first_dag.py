from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id="mera_pehla_dag",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    task_1 = BashOperator(
        task_id="print_hello",
        bash_command="echo 'Airflow start ho gaya!'",
    )

    task_2 = BashOperator(
        task_id="print_success",
        bash_command="echo 'Task successfully chal gaya!'",
    )

    task_1 >> task_2
