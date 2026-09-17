# FraudGuard AI - Credit Card Fraud Detection

FraudGuard AI is a machine learning based project that is designed to detect fraudulent credit card transactions.

The project takes transaction data, processes it, and uses a trained machine learning model to predict whether a transaction is normal or fraudulent. A Streamlit dashboard is also included to make the project easier to use and understand.

## Project Overview

Credit card fraud is a common problem where some transactions may not be made by the actual card holder. Since fraudulent transactions are usually much fewer than normal transactions, detecting them from a large dataset can be challenging.

This project uses machine learning to study transaction data and identify patterns that can help classify transactions into two categories:

- Normal Transaction
- Fraudulent Transaction

The project also includes a simple web dashboard where the dataset and fraud detection results can be viewed.

## Main Features

- Load and analyze credit card transaction data
- Check the dataset before training
- Preprocess the transaction data
- Train a machine learning model
- Save the trained model for prediction
- Scale transaction amount values
- Predict whether a transaction is fraudulent or normal
- Display transaction statistics
- Show normal vs fraudulent transaction distribution
- Interactive Streamlit dashboard

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib
- Matplotlib
- NumPy

## Project Structure

```text
CREDIT-CARD-FRAUD-DETECTION/
│
├── data/
│   └── creditcard.csv
│
├── src/
│   ├── analysis.py
│   ├── app.py
│   ├── check_data.py
│   ├── predict.py
│   ├── train_model.py
│   │
│   └── models/
│       ├── fraud_model.pkl
│       └── scaler.pkl
│
├── requirements.txt
└── README.md
