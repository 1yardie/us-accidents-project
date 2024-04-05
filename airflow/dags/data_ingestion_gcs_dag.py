import datetime
import os

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from google.cloud import storage

storage_client = storage.Client() # Create a storage client
bucket_name = "us-accidents-418522_data_lake" # Define your GCS bucket name
parquet_directory = "data/accidents" # Define the path to the directory of files to upload
bucket = storage_client.bucket(bucket_name) # Get the bucket
key_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

def upload_to_gcs_callable():
    for file_name in os.listdir(parquet_directory):
        #All parquet files imported with spark starts with part....
        if(file_name.startswith("part")):
            
            # The full file path
            local_file_path = os.path.join(parquet_directory, file_name)
            destination_name = f"data/{file_name}"
            
            # Upload the file to the bucket     
            blob = bucket.blob(destination_name)
            blob.upload_from_filename(local_file_path)
            print(f"File {local_file_path} uploaded to {local_file_path} in bucket {bucket_name}.")

# DAG for data ingestion into GCS Bucket
with DAG(
    dag_id="data_ingestion_gcs_dag",
    start_date=datetime.datetime(2024, 1, 1),
    schedule="@yearly",
):
    upload_to_gcs = PythonOperator(
        task_id="upload_to_gcs",
        python_callable=upload_to_gcs_callable
    )

upload_to_gcs