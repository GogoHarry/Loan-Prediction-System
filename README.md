# Loan-Approval-Prediction-System

## Project Overview

![loan1](https://github.com/GogoHarry/Loan-Prediction-System/assets/82883963/76c814d2-ea31-4758-8957-7a068f53c4fa)


This project aims to automate the loan eligibility process for Dream Housing Finance company. The company deals in all kinds of home loans and has a presence across urban, semi-urban, and rural areas. The goal is to build a machine learning model that predicts the loan status (approved or not approved) based on various customer details in the application form.

The project involves data preprocessing, exploratory data analysis, feature engineering, model training, evaluation, and deployment using Flask for a real-time prediction API.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Data Source](#data-source)
3. [Tools](#tools)
4. [Data Description](#data-description)
5. [Descriptive Analysis](#descriptive-analysis)
6. [Data Cleaning](#data-cleaning)
7. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
8. [Model Developement](#model-development)
   - [Logistic Regression](#logistic-regression)
   - [Decision Tree](#decision-tree)
   - [Random Forest](#random-forest)
   - [Gradient Boosting Classifier](#gradient-boosting-classifier)
   - [XGBoost Classifier](#xgboost-classifier)

## Data Source

The dataset used for this project is provided in the data directory. It contains information about the loan applicants.

The dataset contains the following columns:
- Loan_ID: Unique identifier for each loan application.
- Gender: Gender of the applicant.
- Married: Marital status of the applicant.
- Dependents: Number of dependents.
- Education: Educational background of the applicant.
- Self_Employed: Whether the applicant is self-employed.
- ApplicantIncome: Applicant's income.
- CoapplicantIncome: Co-applicant's income.
- LoanAmount: Loan amount in thousands.
- Loan_Amount_Term: Term of the loan in months.
- Credit_History: Credit history meets guidelines.
- Property_Area: Urban, Semi-Urban, or Rural.
- Loan_Status: (Target) Whether the loan was approved (Y/N) or unapproved



