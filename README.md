# Accident Data Analysis Project

Link to Dashboard: [Link](https://lookerstudio.google.com/reporting/5b6c6190-8d71-448d-84bd-a615e5a8652b)
## Overview
The goal of the US Accidents Data Analysis Project is to use Data Engineering concepts to automate a workflow to download the US Accidents Dataset (February 2016 to March 2023) from Kaggle to Google Cloud Storage, transform and aggregate the data using DBT and analyze it using Looker Studio. The ELT (Extract, Load and Transform) methodology is used through out this project where data is extracted, loaded and then transformed in the Data Warehouse. 

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
The project was created entirely on a Google Cloud Storage (GCS) Virtual Machine in the cloud. The VM provided a scalable and flexible environment for developing and running the project.

## Kaggle API
The US Car Accident dataset from 49 states of the USA, collected from February 2016 to March 2023, was downloaded using the Kaggle API. This dataset consists of 3GB of data and approximately 7.7 million rows.

## Terraform
Terraform was used for Infrastructure Provisioning on Google Cloud Platform. It facilitated the creation and management of resources, including Google Cloud Storage buckets, required for the project.

## Spark
Spark was used for data processing tasks due to its distributed computing capabilities. It enabled efficient processing of large-scale data and analytics tasks.

## Apache Airflow
Apache Airflow is used for workflow orchestration and automation. It is deployed inside a Docker container for easy management and scalability.

## Google Cloud Storage Buckets (Data Lake)
Data downloaded using the Kaggle API is uploaded to a Google Cloud Storage Bucket, serving as a Data Lake. Google Cloud Storage provides scalable, durable, and highly available object storage suitable for storing large datasets.

## BigQuery (Data Warehouse)
BigQuery is used as the Data Warehouse for storing and querying structured data. It offers high-performance SQL queries and integrates seamlessly with other Google Cloud Platform services.

## Python
Python programming language is used for various data processing tasks, scripting, and automation within the project.

## SQL
SQL is utilized for querying and manipulating data in BigQuery and performing transformations on the data.

## Acknowledgements
Moosavi, Sobhan, Mohammad Hossein Samavatian, Srinivasan Parthasarathy, and Rajiv Ramnath. “A Countrywide Traffic Accident Dataset.”, 2019.

Moosavi, Sobhan, Mohammad Hossein Samavatian, Srinivasan Parthasarathy, Radu Teodorescu, and Rajiv Ramnath. "Accident Risk Prediction based on Heterogeneous Sparse Data: New Dataset and Insights." In proceedings of the 27th ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems, ACM, 2019.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
