import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator


with DAG(
    dag_id="data_ingestion_gcs_local",
    start_date=datetime.datetime(2021, 1, 1),
    schedule="@daily",
):
    first_task = EmptyOperator(task_id="first_task")
    second_task = EmptyOperator(task_id="second_task")

    first_task >> second_task