import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Load dataset
data = pd.read_csv("data/creditcard.csv")

print("Dataset loaded!")
print("Shape:", data.shape)

# Separate features and target
X = data.drop("Class", axis=1)
y = data["Class"]

# Scale the Amount column
scaler = StandardScaler()
X["Amount"] = scaler.fit_transform(X[["Amount"]])

# Remove Time column
X = X.drop("Time", axis=1)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining data:", X_train.shape)
print("Testing data:", X_test.shape)

# Create model
model = LogisticRegression(max_iter=1000)

# Train model
print("\nTraining model...")
model.fit(X_train, y_train)

print("Model training completed!")

# Make predictions
y_pred = model.predict(X_test)

# Results
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
import joblib

# Save the trained model
joblib.dump(model, "src/models/fraud_model.pkl")
joblib.dump(scaler, "src/models/scaler.pkl")
print("\nModel saved successfully!")