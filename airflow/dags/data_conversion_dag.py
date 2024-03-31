import pyspark
from pyspark.sql import SparkSession
import os 
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

local_workflow = DAG(
    dag_id="data_conversion_dag",
    default_args={
        'owner': 'airflow',
        'start_date': datetime(2024, 3, 30),
        'schedule': "@yearly"
    }
)

def spark_read_write_file():
    spark = SparkSession.builder \
        .master("local[*]") \
        .appName('test') \
        .getOrCreate()

    # #Read CSV file to Spark Dataframe
    df = spark.read \
        .format("csv") \
        .option("header","true") \
        .load("data/accidents.csv")
    df.write.parquet("/opt/airflow/data/accidents")

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