# Loan-Status-Prediction-System

### Project Video

<video src="https://private-user-images.githubusercontent.com/82883963/353051231-7cf24d63-4f46-472f-88f0-cc82e4b89141.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjIyNTYyMjAsIm5iZiI6MTcyMjI1NTkyMCwicGF0aCI6Ii84Mjg4Mzk2My8zNTMwNTEyMzEtN2NmMjRkNjMtNGY0Ni00NzJmLTg4ZjAtY2M4MmU0Yjg5MTQxLm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA3MjklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNzI5VDEyMjUyMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWVlNDA2OTViZWJlZjMxNzZmMDc3ZmFkZDQ0OWQxMzBlOTJjYzFkMGQ4ZmYwM2M1ZGVjNWYwM2VkYzNjNDc3Y2UmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.BGyDL4rAmTytjLBfaE79oEFomE__TmKSA7EYvFH2uqc" controls="controls" style="max-width: 100%;">
</video>

## Project Overview

This project aims to develop a machine learning-based system using various customer details to predict the loan application approval status. It leverages historical data and supervised learning techniques to make reliable predictions, serving as a decision-support tool for lenders.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Model Training](#model-training)
- [Evaluation](#evaluation)
- [Web Application](#web-application)
- [Contributing](#contributing)
- [License](#license)

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/GogoHarry/Loan/loan-prediction-system.git
    cd loan-prediction-system
    ```
2. Create a virtual environment:
    ```bash
    python -m venv loan_prediction_venv
    ```
3. Activate the virtual environment:
    - On Windows:
        ```bash
        loan_prediction_venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source loan_prediction_venv/bin/activate
        ```
4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Train the model and save the preprocessor and model:
    ```bash
    python train_model.py
    ```
2. Run the Streamlit web application:
    ```bash
    streamlit run app.py
    ```

## Features
- Predict loan approval status based on customer details.
- Preprocess data using a fitted pipeline.
- Web interface for user-friendly interaction.

## Model Training
1. Preprocess the data using `OneHotEncoder` and `StandardScaler`.
2. Train the RandomForest model and save the preprocessor and model.

## Evaluation
```python
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

# Load the model
model_pipeline = joblib.load('best_rf_model.pkl')

# Predict and evaluate
predictions = model_pipeline.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f'Accuracy: {accuracy:.2f}')
print('Classification Report:')
print(classification_report(y_test, predictions))
print('Confusion Matrix:')
print(confusion_matrix(y_test, predictions))
```

# Web Application
1. Run the Streamlit app
```bash
streamlit run app.py
```

2. The app will be accessible at http://localhost:8501. Provide input data and get loan eligibility predictions.

# Contributing
1. Fork the repository.
2. Create a new branch:
```bash
git checkout -b feature-branch
```
3. Commit your changes:
```bash
git commit -m "Add feature"
```
4. Push to the branch:
```bash
git push origin feature-branch
```
5. Create a pull request.

# License
This project is licensed under the MIT License - See the [LICENSE](LICENSE) file for details.
