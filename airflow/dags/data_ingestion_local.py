# Importing libraries and modules
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

import os 

# Setting AIRFLOW_HOME environment variable
AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")

# Defining a local workflow using Airflow
local_workflow = DAG(
    dag_id="data_ingestion_gcs_local",
    default_args={
        'owner': 'airflow',
        'start_date': datetime(2024, 1, 1),
        'schedule': "@yearly"
    }
)

# Defining tasks within the DAG
with local_workflow: 

    #Download the files from Kaggle
    download_dataset = BashOperator(
        task_id="download_data",

        #Bash command to download and unzip the dataset file
        bash_command='kaggle datasets download -d sobhanmoosavi/us-accidents -p /opt/airflow/data --unzip',
    )

    move_dataset = BashOperator(
        task_id="move_data",

        #Renames the dataset to accidents.csv in the data folder
        bash_command='mv /opt/airflow/data/*.csv /opt/airflow/data/accidents.csv',
    )
download_dataset >> move_dataset