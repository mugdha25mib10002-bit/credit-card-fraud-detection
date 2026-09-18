import pandas as pd

print("====================================")
print("CREDIT CARD FRAUD DETECTION PROJECT")
print("====================================")

data = pd.read_csv("data/creditcard.csv")

print("\nDataset loaded successfully!")
print("Dataset shape:", data.shape)

print("\nFirst 5 rows:")
print(data.head())

print("\nColumn names:")
print(data.columns.tolist())

print("\nMissing values:")
print(data.isnull().sum().sum())

print("\nClass distribution:")
print(data["Class"].value_counts())