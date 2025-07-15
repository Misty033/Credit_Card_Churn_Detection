# Credit Card Churn Detection

This project builds a machine learning pipeline to predict customer churn based on credit card usage patterns. It includes model training, evaluation, and a deployed application with both FastAPI and Streamlit interfaces. The solution is fully containerized using Docker and deployable on AWS EC2.

## Key Features

- **0.89 Macro F1 Score** on test data for churn prediction  
- **End-to-End ML Pipeline**: Data preprocessing, feature engineering, model training and evaluation  
- **Streamlit Frontend**: Interactive UI for CSV file predictions  
- **FastAPI Backend**: Lightweight REST API for batch prediction  
- **Dockerized**: Easily portable and reproducible environments  
- **Deployed on AWS EC2**: Live application hosted in the cloud  

## Tech Stack

- **Language**: Python  
- **ML Frameworks**: scikit-learn, pandas, numpy  
- **Web App**: Streamlit  
- **API**: FastAPI  
- **DevOps**: Docker, Docker Compose, Git, EC2 (Ubuntu)  
- **Version Control**: Git & GitHub  

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Misty033/Credit_Card_Churn_Detection.git
   cd Credit_Card_Churn_Detection
   ```

2. Build and run with Docker Compose:
   ```bash
   docker compose up --build
   ```

3. Access:
   - Streamlit app: http://52.66.185.212:8501
   - FastAPI docs: http://52.66.185.212:8000/docs

## Sample Input CSV

    You can download the sample input file to test the application:

    [Download sample_input.csv](https://github.com/Misty033/Credit_Card_Churn_Detection/blob/main/file.csv)


## Authors

- Misty Roy  
- Ashish Kar