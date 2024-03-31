import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from google.cloud import bigquery

def upload_to_bigquery_callable():

    # Construct a BigQuery client object.
    client = bigquery.Client()

    # Set the destination table ID.
    table_id = "us-accidents-418522.us_accidents.accidents"

    #Job config 
    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        source_format=bigquery.SourceFormat.PARQUET,
    )

    #URI to load parquet data from
    uri = "gs://us-accidents-418522_data_lake/data/*"

    # Load data into destination table.
    load_job = client.load_table_from_uri(
        uri, table_id, job_config=job_config
    )  

    # Wait for the job to complete.
    load_job.result()  

    # Retrieve information about the destination table.
    destination_table = client.get_table(table_id)

    # Print the number of rows loaded into the destination table.
    print("Loaded {} rows.".format(destination_table.num_rows))


with DAG(
    dag_id="data_ingestion_bigquery_dag",
    start_date=datetime.datetime(2024, 1, 1),
    schedule="@yearly",
):
    upload_to_bigquery = PythonOperator(
        task_id="python_task",
        python_callable=upload_to_bigquery_callable,
    )
upload_to_bigquery_callable
