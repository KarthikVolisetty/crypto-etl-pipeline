# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 14:10:32 2024

@author: karth
"""

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from scripts.fetch_data import fetch_data
from scripts.transform_data import transform_data
from scripts.load_data import load_data

def etl():
    data = fetch_data()
    transformed_data = transform_data(data)
    load_data(transformed_data)

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# Define the DAG
with DAG(
    dag_id='crypto_etl_pipeline',
    default_args=default_args,
    description='A simple ETL pipeline for crypto data',
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False
) as dag:

    etl_task = PythonOperator(
        task_id='run_etl',
        python_callable=etl
    )