# FraudGuard AI - Credit Card Fraud Detection

## Project Overview

FraudGuard AI is a machine learning project that is designed to detect potentially fraudulent credit card transactions.

The main idea of this project is to use transaction data to train a machine learning model and then use the trained model to classify transactions as either normal or fraudulent.

The project also includes a Streamlit web application where the dataset can be explored and fraud detection results can be viewed through a simple dashboard.

## Features

The project includes the following features:

- Credit card transaction dataset analysis
- Data checking and preprocessing
- Machine learning model training
- Fraud and normal transaction classification
- Transaction prediction using the trained model
- Interactive Streamlit dashboard
- Transaction statistics and visualizations
- Dataset analysis
- Separate scripts for checking data, training the model, and making predictions

## Technologies and Tools Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib
- Pickle
- VS Code
- Git and GitHub

## Project Structure

```text
CREDIT-CARD-FRAUD-DETECTION/
│
├── data/
│   └── creditcard.csv
│
├── src/
│   ├── app.py
│   ├── analysis.py
│   ├── check_data.py
│   ├── predict.py
│   ├── train_model.py
│   │
│   └── models/
│       ├── fraud_model.pkl
│       └── scaler.pkl
│
├── README.md
├── statement.md
├── requirements.txt
└── .gitignore









Installation
1. Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL
2. Open the project folder
cd CREDIT-CARD-FRAUD-DETECTION
3. Create a virtual environment
python -m venv venv
4. Activate the virtual environment

On Windows:

venv\Scripts\activate
5. Install the required packages
pip install -r requirements.txt
Running the Project

To start the Streamlit web application, run:

streamlit run src/app.py

The application will open in the browser and display the FraudGuard AI dashboard.

Running the Individual Scripts
Check the dataset
python src/check_data.py
Run dataset analysis
python src/analysis.py
Train the model
python src/train_model.py
Make a prediction
python src/predict.py
Testing Instructions

The project can be tested by running the Streamlit application and checking the different sections of the dashboard.

Basic testing steps:

Start the application using:
streamlit run src/app.py
Open the application in the browser.
Check the dashboard statistics.
Check the transaction distribution shown in the application.
Open the fraud detection section.
Test the prediction functionality using transaction data.
Check whether the application displays the predicted result correctly.
Screenshots

Screenshots of the Streamlit dashboard can be added here to show the working project.

Example:

Dashboard screenshot
Fraud Detection screenshot
Dataset Analysis screenshot
Future Improvements

Some improvements that can be added to the project in the future are:

Add more machine learning models and compare their performance.
Add accuracy and other evaluation metrics to the dashboard.
Allow users to enter transaction details directly.
Add a confusion matrix and classification report.
Improve the dashboard design.
Add real-time transaction monitoring.
Deploy the application online.
Limitations

This project is mainly intended for learning and demonstration purposes.

The prediction depends on the dataset and the trained machine learning model. A real-world fraud detection system would require more data, continuous monitoring, regular model evaluation, and additional security measures.

Conclusion

FraudGuard AI demonstrates how machine learning can be applied to a real-world problem such as credit card fraud detection.

The project covers the basic workflow from checking and analyzing the data to preparing the features, training a model, making predictions, and displaying the results through a Streamlit web application.

This project helped us understand how Python, data analysis, machine learning, and a simple web interface can be combined to build a practical application.

Author

Credit Card Fraud Detection Project

Built using Python, Machine Learning, and Streamlit.
