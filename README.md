# Customer Churn Prediction & Lifetime Value (LTV) Engine

## Project Overview

This project is a production-style data analytics and machine learning system developed for predicting customer churn and analyzing Customer Lifetime Value (LTV) in a telecom business environment.

The system uses historical customer data such as:

* Customer demographics
* Billing information
* Contract details
* Internet services
* Tenure and monthly charges

Using this data, the model predicts:

1. Whether a customer is likely to churn
2. Customer Lifetime Value (LTV)

The project also includes:

* Explainable AI using SHAP
* PostgreSQL data warehouse integration
* FastAPI deployment
* Batch prediction system
* Power BI dashboard integration

---

# Problem Statement

Telecom companies lose customers due to churn, which increases customer acquisition costs.

This project helps businesses:

* Identify customers at high risk of churn
* Improve retention strategies
* Optimize marketing campaigns
* Focus on high-value customers

---

# Tech Stack

## Programming Languages

* Python
* SQL

## Machine Learning

* Pandas
* Scikit-learn
* XGBoost
* SHAP

## Deployment

* FastAPI
* Uvicorn

## Database

* PostgreSQL
* SQLAlchemy

## Visualization

* Power BI

## Version Control

* GitHub

---

# Project Architecture

Dataset
→ Data Cleaning & Preprocessing
→ Exploratory Data Analysis (EDA)
→ Feature Engineering
→ XGBoost Model Training
→ SHAP Explainability
→ LTV Segmentation
→ PostgreSQL Storage
→ FastAPI Deployment
→ Power BI Dashboard

---

# Dataset Information

Dataset Used:

* Telco Customer Churn Dataset

Dataset contains:

* Customer demographics
* Phone services
* Internet services
* Monthly charges
* Total charges
* Contract types
* Churn information

---

# Features Implemented

## 1. Customer Churn Prediction

* Predicts whether customer will churn or not
* Binary classification problem

## 2. LTV Engine

* Calculates customer lifetime value
* Segments customers based on value

## 3. SHAP Explainability

* Explains why the model predicts churn
* Visual feature importance analysis

## 4. Batch Prediction

* Predicts churn for new customer CSV files

## 5. FastAPI Deployment

* REST API for live predictions
* Swagger documentation support

## 6. PostgreSQL Integration

* Stores processed customer data in database
* Supports dashboard and analytics workflows

## 7. Power BI Dashboard

* KPI visualization
* Churn analytics
* Business insights

---

# Machine Learning Model

Model Used:

* XGBoost Classifier

Evaluation Metrics:

* Accuracy
* Precision
* Recall
* F1-score

---

# API Endpoints

## Home Endpoint

GET /

Returns API status.

## Prediction Endpoint

GET /test

Returns churn prediction for sample customer.

---

# PostgreSQL Integration

Database Name:

* customer_churn_db

Table Name:

* customers

---

# Power BI Dashboard Insights

The dashboard includes:

* Total Customers
* Total Churn Customers
* Churn Rate
* Churn by Contract Type
* Churn by Internet Service
* LTV Segmentation
* Customer Retention Insights

---

# Project Outcomes

* Improved churn understanding
* Business-focused customer segmentation
* Explainable machine learning predictions
* Production-style API deployment
* Data warehouse integration

---

# Future Improvements

* Real-time prediction API
* Cloud deployment
* Automated retraining pipeline
* Advanced customer segmentation
* Docker deployment

---

# GitHub Repository

Project Repository:
[https://github.com/alapatirohith91/customer-churn-prediction](https://github.com/alapatirohith91/customer-churn-prediction)

---

# Author

Rohith Alapati
B.Tech Student | Data Analytics Enthusiast
