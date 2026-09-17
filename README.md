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

How the Project Works

The project is divided into a few simple steps.

1. Dataset

The credit card transaction dataset is stored inside the data folder.

The dataset contains transaction information along with a Class column. This column is used to identify whether a transaction belongs to the normal or fraudulent class.

2. Data Checking

The check_data.py file is used to check the dataset and understand the data before using it for machine learning.

3. Data Analysis

The analysis.py file is used to perform basic analysis and understand the distribution of transactions in the dataset.

4. Model Training

The train_model.py file is used to train the machine learning model using the available transaction data.

After training, the model is saved inside:

src/models/

The saved files include:

fraud_model.pkl
scaler.pkl
5. Prediction

The predict.py file loads the trained model and uses it to check a transaction.

The final result is displayed as either:

RESULT: NORMAL TRANSACTION

or

RESULT: FRAUDULENT TRANSACTION
6. Web Application

The app.py file contains the Streamlit application.

The dashboard provides a simple interface for viewing information about the dataset and the fraud detection system.

Dashboard

The dashboard includes:

Total number of transactions
Number of normal transactions
Number of fraudulent transactions
Transaction distribution chart
Fraud detection section
Dataset analysis section

The dashboard is designed to give a quick overview of the dataset and the results of the fraud detection system.

Machine Learning Workflow

The basic workflow used in this project is:

Credit Card Dataset
        ↓
Data Checking
        ↓
Data Preprocessing
        ↓
Feature Preparation
        ↓
Model Training
        ↓
Trained Model
        ↓
Transaction Input
        ↓
Prediction
        ↓
Normal / Fraudulent
Dataset

The project uses a credit card transaction dataset containing transaction features and a target class.

The Class value represents the transaction category used for the prediction task.

The dataset contains a large number of transactions, with normal transactions making up most of the data and fraudulent transactions representing a much smaller portion.

Why Machine Learning?

Manually checking a large number of transactions is difficult and time-consuming.

Machine learning can learn patterns from previous transaction data and use those patterns to classify new transactions. This makes it useful for applications such as fraud detection, where large amounts of transaction data need to be analyzed.

Future Improvements

Some improvements that can be added to the project in the future are:

Add more machine learning models and compare their performance
Add model accuracy and other evaluation metrics to the dashboard
Allow users to enter transaction details directly
Add a confusion matrix and classification report
Improve the dashboard design
Add real-time transaction monitoring
Deploy the application online
Limitations

This project is mainly intended for learning and demonstration purposes.

The prediction depends on the dataset and the trained machine learning model. A real-world fraud detection system would require much more data, continuous monitoring, model evaluation, and additional security measures.

Conclusion

FraudGuard AI demonstrates how machine learning can be used for credit card fraud detection.

The project covers the complete basic workflow, starting from data checking and analysis, followed by model training and prediction, and finally presenting the results through a Streamlit web application.

It was developed as a practical project to understand how machine learning can be applied to a real-world problem such as credit card fraud detection.

Author

Credit Card Fraud Detection Project

Built using Python and Machine Learning.
