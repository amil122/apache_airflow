"""
In this DAG, we perform basic math operations in the following sequence:
task 1: Start with initial number (e.g., 10)
task 2: Add 5 to the number
task 3: Multiply the result by 2
task 4: Subtract 3 from the result
task 5: Compute the square root of the final result
"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import math

# ---- Task Functions ----

def start_number(**context):
    context["ti"].xcom_push(key="current_value", value=10)
    print("Starting with number 10")

def add_five(**context):
    current_value = context["ti"].xcom_pull(key="current_value", task_ids="start_task")
    new_value = current_value + 5
    context["ti"].xcom_push(key="current_value", value=new_value)
    print(f"Adding 5: {current_value} + 5 = {new_value}")

def multiply(**context):
    current_value = context["ti"].xcom_pull(key="current_value", task_ids="add_five_task")
    new_value = current_value * 2
    context["ti"].xcom_push(key="current_value", value=new_value)
    print(f"Multiplied by 2: {current_value} * 2 = {new_value}")

def subtract(**context):
    current_value = context["ti"].xcom_pull(key="current_value", task_ids="multiply_by_two_task")
    new_value = current_value - 3
    context["ti"].xcom_push(key="current_value", value=new_value)
    print(f"Subtracting 3: {current_value} - 3 = {new_value}")

def square_root(**context):
    current_value = context["ti"].xcom_pull(key="current_value", task_ids="subtract_three_task")
    new_value = math.sqrt(current_value)
    print(f"Square root of result: √{current_value} = {new_value}")


# ---- DAG Definition ----
with DAG(
    dag_id="math_sequence_dag",
    start_date=datetime.today(),
    schedule="@once",
    catchup=False            # Prevent backfilling
) as dag:

    start_task = PythonOperator(
        task_id="start_task",
        python_callable=start_number,
        
    )

    add_five_task = PythonOperator(
        task_id="add_five_task",
        python_callable=add_five
    )

    multiply_task = PythonOperator(
        task_id="multiply_by_two_task",
        python_callable=multiply
    )

    subtract_task = PythonOperator(
        task_id="subtract_three_task",
        python_callable=subtract
    )

    square_root_task = PythonOperator(
        task_id="square_root_task",
        python_callable=square_root
    )

    # ---- Task Dependencies ----
    start_task >> add_five_task >> multiply_task >> subtract_task >> square_root_task
