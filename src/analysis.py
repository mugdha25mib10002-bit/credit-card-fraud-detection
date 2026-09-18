import pandas as pd
import matplotlib.pyplot as plt

print("CREDIT CARD FRAUD DETECTION - DATA ANALYSIS")
print("=" * 50)

# Load dataset
data = pd.read_csv("data/creditcard.csv")

print("\nDataset Shape:")
print(data.shape)

print("\nDataset Information:")
print(data.info())

print("\nStatistical Summary:")
print(data.describe())

# Class distribution
print("\nClass Distribution:")
print(data["Class"].value_counts())

# Fraud percentage
fraud_percentage = data["Class"].mean() * 100

print("\nFraud Percentage:")
print(f"{fraud_percentage:.4f}%")

# Transaction amount
print("\nTransaction Amount Statistics:")
print(data["Amount"].describe())

# -----------------------------
# Fraud vs Normal Chart
# -----------------------------

class_counts = data["Class"].value_counts()

plt.figure(figsize=(7, 5))
plt.bar(
    ["Normal", "Fraud"],
    [class_counts.get(0, 0), class_counts.get(1, 0)]
)

plt.title("Normal vs Fraudulent Transactions")
plt.xlabel("Transaction Type")
plt.ylabel("Number of Transactions")

plt.tight_layout()
plt.show()

# -----------------------------
# Transaction Amount Chart
# -----------------------------

plt.figure(figsize=(8, 5))

plt.hist(data["Amount"], bins=50)

plt.title("Transaction Amount Distribution")
plt.xlabel("Transaction Amount")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

print("\nAnalysis completed successfully!")