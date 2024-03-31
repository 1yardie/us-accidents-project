import wget
import pyspark
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
from pyspark.context import SparkContext
from google.cloud import storage
from google.cloud import bigquery


storage_client = storage.Client() # Create a storage client
bucket_name = "us-accidents-418522_data_lake" # Define your GCS bucket name
parquet_directory = "data/accidents" # Define the path to the directory of files to upload
bucket = storage_client.bucket(bucket_name) # Get the bucket


def init_spark():
    #Start Spark Session
    spark = SparkSession.builder \
        .appName('test') \
        .getOrCreate()

def spark_read_file():
    #Read CSV file to Spark Dataframe
    df = spark.read \
        .format("csv") \
        .option("header","true") \ 
        .load("data/accidents.csv") \

def spark_write_parquet():
    #Write spark Dataframe to Parquet files
    df.write.parquet("data/accidents")

def upload_to_gcs():
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
    
def upload_to_bigquery():
    # Construct a BigQuery client object.
    client = bigquery.Client()

    # TODO(developer): Set table_id to the ID of the table to create.
    table_id = "us-accidents-418522.us_accidents.accidents"

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.PARQUET,
    )
    uri = "gs://us-accidents-418522_data_lake/data/*"

    load_job = client.load_table_from_uri(
        uri, table_id, job_config=job_config
    )  # Make an API request.

    load_job.result()  # Waits for the job to complete.

    destination_table = client.get_table(table_id)
    print("Loaded {} rows.".format(destination_table.num_rows))

