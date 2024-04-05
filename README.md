# Accident Data Analysis Project

Link to Dashboard: [Link](https://lookerstudio.google.com/reporting/5b6c6190-8d71-448d-84bd-a615e5a8652b)
## Overview
The goal of the US Accidents Data Analysis Project is to use Data Engineering concepts to automate a workflow to download the US Accidents Dataset (February 2016 to March 2023) from Kaggle to Google Cloud Storage, transform and aggregate the data using DBT and analyze it using Looker Studio. The ELT (Extract, Load and Transform) methodology is used through out this project where data is extracted, loaded and then transformed in the Data Warehouse. The end result is a dashboard that shows the accidents ranked by state, severity, time zone etc.

## Pipeline 

![Google Cloud Virtual Machine (1)](https://github.com/1yardie/us-accidents-project/assets/162933913/e24f574c-d8d0-484c-b92c-de04d138da0a)


## Technologies

The project utilizes a range of cutting-edge technologies and tools:

- Apache Airflow
- DBT
- Google Cloud Storage
  - Virtual Machine
  - Data Lake (Buckets)
  - Data Warehouse (BigQuery)
- Docker
- Spark
- Pandas (Testing)
- Looker Studio
- Kaggle API
- SQL


## ELT Methodology
The project follows an ELT (Extract, Load, Transform) methodology. Data is first extracted from the Data Lake, loaded into BigQuery, and then transformed and aggregated using dbt (Data Build Tool).

## Google Cloud Storage Virtual Machine (VM)
The project was created entirely on a Google Cloud Storage (GCS) Virtual Machine in the cloud. The VM provided a scalable and flexible environment for developing and running the project. The US Car Accident dataset from 49 states of the USA, collected from February 2016 to March 2023, was downloaded using the Kaggle API. This dataset consists of 3GB of data and approximately 7.7 million rows. Terraform was used for Infrastructure Provisioning on Google Cloud Platform. It facilitated the creation and management of resources, including Google Cloud Storage buckets, required for the project. Spark was used for data processing tasks due to its distributed computing capabilities. It enabled efficient processing of large-scale data and analytics tasks. Apache Airflow is used for workflow orchestration and automation. It is deployed inside a Docker container for easy management and scalability.

## Google Cloud Storage Buckets (Data Lake)
Data downloaded using the Kaggle API is uploaded to a Google Cloud Storage Bucket, serving as a Data Lake and BigQuery is used as the Data Warehouse for storing and querying structured data. SQL is utilized for querying and manipulating data in BigQuery and performing transformations on the data.

## Setup
Link to dashboard: [Link](https://lookerstudio.google.com/reporting/5b6c6190-8d71-448d-84bd-a615e5a8652b)
I haven't gotten around to testing this set up on another machine but I believe it should work by following these steps:

- Clone the project repository to your local machine.
- Ensure you have access to Google Cloud Platform services, including Google Cloud Storage, BigQuery, and Compute Engine.
- Install any necessary dependencies specified in the requirements file.
- Kaggle API credentials will be needed to download the dataset. Sign up on Kaggle and put your Kaggle credentials in docker-compose.yaml and airflow/scripts/entrypoint.sh.
- Run docker-compose build
- Run docker-compose up airflow-init
- Run docker-compose up
- Run the code and explore the dashboard to view the analysis results.

## Future Plans
This will be an ongoing project with new features being added.

Todo:
- Test setups on other machines
- Use Tableau for Data Visualization

## Acknowledgements
Moosavi, Sobhan, Mohammad Hossein Samavatian, Srinivasan Parthasarathy, and Rajiv Ramnath. “A Countrywide Traffic Accident Dataset.”, 2019.

Moosavi, Sobhan, Mohammad Hossein Samavatian, Srinivasan Parthasarathy, Radu Teodorescu, and Rajiv Ramnath. "Accident Risk Prediction based on Heterogeneous Sparse Data: New Dataset and Insights." In proceedings of the 27th ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems, ACM, 2019.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
