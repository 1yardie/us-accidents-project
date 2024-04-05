#Import libraries
import pyspark
from pyspark.sql import SparkSession
import os 
from datetime import datetime

#Import modules from Airflow
from airflow import DAG
from airflow.operators.python import PythonOperator

#Define local workflow in Airflow
local_workflow = DAG(
    dag_id="data_conversion_dag",
    default_args={
        'owner': 'airflow',
        'start_date': datetime(2024, 1, 1),
        'schedule': "@yearly"
    }
)

# Read CSV file and write to Parquet format using PySpark
def spark_read_write_file():
    #Create a SparkSession
    spark = SparkSession.builder \
        .master("local[*]") \
        .appName('test') \
        .getOrCreate()

    #Read the CSV file to a Spark Dataframe
    df = spark.read \
        .format("csv") \
        .option("header","true") \
        .load("data/accidents.csv")
    
    #Write Dataframe to Parquet format
    df.write.parquet("/opt/airflow/data/accidents")

# Add tasks to the workflow using PythonOperator

with local_workflow:
    convert_to_parquet = PythonOperator(
        task_id="python_task",
        python_callable=spark_read_write_file,
        # op_kwargs: Optional[Dict] = None,
        # op_args: Optional[List] = None,
        # templates_dict: Optional[Dict] = None
        # templates_exts: Optional[List] = None
    )
convert_to_parquet