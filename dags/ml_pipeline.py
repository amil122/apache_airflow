from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Define task 1
def preprocess_data():
    print("Started preprocessing the data")

# Define task 2
def train_model():
    print("Started the training using the processed data")

# Define task 3
def evaluate_model():
    print("Evaluation of the trained model")

# DAG Definition
with DAG(
    dag_id="ml_pipeline_for_training",
    start_date=datetime(2025, 10, 1),
    schedule="@daily",  
    catchup=False
) as dag:
    
    preprocess = PythonOperator(
        task_id="preprocessing_step",
        python_callable=preprocess_data
    )
    
    train = PythonOperator(
        task_id="model_training",
        python_callable=train_model
    )
    
    evaluate = PythonOperator(
        task_id="evaluation_model",
        python_callable=evaluate_model
    )
    
    # Setting dependencies
    preprocess >> train >> evaluate
