# ============================================================
# train_model.py - Train and Save the Heart Disease ML Model
# ============================================================

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
import pickle

# ============================================================
# Load the dataset
# ============================================================
df = pd.read_csv('dataset/heart.csv')

# ============================================================
# Separate features (X) and target (y)
# ============================================================
X = df.drop('target', axis=1)  # All columns except 'target'
y = df['target']               # The target column (0 or 1)

# ============================================================
# Split into training (80%) and testing (20%) sets
# ============================================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ============================================================
# Scale the features for better model performance
# ============================================================
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)  # Fit and transform training data
X_test = scaler.transform(X_test)        # Only transform test data

# ============================================================
# Train the Random Forest model
# ============================================================
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ============================================================
# Evaluate the model
# ============================================================
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print(classification_report(y_test, y_pred))

# ============================================================
# Save the model and scaler together
# ============================================================
with open('model.pkl', 'wb') as f:
    pickle.dump((model, scaler), f)

print("Model saved as model.pkl")




