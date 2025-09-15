# Apache Airflow with Astronomer - Local Setup

## 🚀 Overview
This project provides a **local development environment** for building, testing, and running **Apache Airflow DAGs** using **Astronomer**.  
It is designed to help me develop and test ETL workflows, ML pipelines, and other data engineering tasks **before pushing them to production**.

---

## 📂 Project Structure
| Folder/File            | Purpose |
|------------------------|---------|
| `dags/`               | Contains all custom Airflow DAGs. <br> _Example_: `example_astronauts.py` demonstrates a simple ETL workflow using TaskFlow API. |
| `Dockerfile`           | Defines the Airflow runtime environment using Astronomer's **Astro Runtime image**. |
| `requirements.txt`     | List of Python dependencies for DAGs. |
| `packages.txt`         | OS-level packages required for the project. |
| `plugins/`             | Custom or third-party Airflow plugins. |
| `airflow_settings.yaml`| Configure local Airflow **connections**, **variables**, and **pools**. |

---

## 🛠️ Running Airflow Locally

### 1. **Start Airflow**
```bash
astro dev start
