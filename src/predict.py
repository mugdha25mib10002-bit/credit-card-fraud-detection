import pandas as pd
import joblib

# Load the trained model
model = joblib.load("src/models/fraud_model.pkl")

print("====================================")
print("     CREDIT CARD FRAUD DETECTION")
print("====================================")

# Load the dataset
data = pd.read_csv("data/creditcard.csv")

# Select one transaction from the dataset
transaction = data.iloc[[0]].copy()

# Remove the target column
transaction = transaction.drop("Class", axis=1)

# Scale Amount in the same way as training
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(data[["Amount"]])
transaction["Amount"] = scaler.transform(transaction[["Amount"]])

# Remove Time
transaction = transaction.drop("Time", axis=1)

# Make prediction
prediction = model.predict(transaction)

print("\nTransaction checked!")

if prediction[0] == 1:
    print("RESULT: FRAUDULENT TRANSACTION")
else:
    print("RESULT: NORMAL TRANSACTION")