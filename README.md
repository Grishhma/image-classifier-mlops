# 🖼️ Image Classifier MLOps Pipeline

An end-to-end MLOps workflow: train a PyTorch model, track with MLflow, package in Docker, and schedule daily retraining via Airflow.



## 🔍 Overview

This project demonstrates a production-ready pipeline for image classification:

1. **Model**: Transfer-learning on ResNet-18 (PyTorch)  
2. **Tracking**: MLflow logs params, metrics & artifacts  
3. **Containerization**: Docker ensures reproducibility  
4. **Orchestration**: Airflow DAG runs `docker run` daily  



## 🛠️ Tech Stack

- **PyTorch** – model definition & training  
- **MLflow** – experiment tracking & artifact storage  
- **Docker** – container runtime  
- **Apache Airflow** – DAG scheduling  
- **Docker Compose** – stand up Airflow services  



## 🏗️ Architecture Diagram

```text
+-----------+      +---------+      +---------+      +-------------+
| PyTorch   | ---> | MLflow  | ---> | Docker  | ---> | Airflow DAG |
| train.py  |      | UI:5000 |      | image-  |      | schedule    |
+-----------+      +---------+      | classifier |  
                                      +---------+
```

# 🚀 Quick Start
1. Clone & Prepare
- git clone https://github.com/Grishhma/image-classifier-mlops.git
- cd image-classifier-mlops
2. Python Environment
- .\venv\Scripts\Activate.ps1
- pip install -r requirements.txt
3. Train Locally
- python src/train.py
4. Dockerized Run
-  docker build -t image-classifier .
-  docker run --rm image-classifier
- docker run --rm -v "${PWD}:/app" image-classifier
5. Schedule with Airflow
- cd airflow
-  docker-compose up
- Airflow UI: http://localhost:8080
- Default Credentials:
- Username: admin
- Password: shown in the container logs
  
# 🔍 How It Works
1. Training Script (src/train.py):
- Loads a FakeData dataset (swap in your real images later)
- Sets up a ResNet-18 backbone, fine-tunes for 2 classes
- Logs params & loss metrics to MLflow
- Saves model checkpoint (resnet18.pth) and logs it as an artifact

2. Dockerfile:
- Starts from python:3.10-slim
- Installs all dependencies (requirements.txt)
- Copies source code and runs python src/train.py on startup

3. Airflow DAG (airflow/dags/retrain_dag.py):
- A simple BashOperator that runs the above Docker image
- Mounted volume persists model and MLflow logs on the host
- Scheduled at @daily by default

  


