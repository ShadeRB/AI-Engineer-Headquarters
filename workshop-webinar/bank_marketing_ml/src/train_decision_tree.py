import pandas as pd
import numpy as np
import os
import joblib
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier

# === Dynamic path setup ===
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(ROOT_DIR)

# === Load data ===
data_path = os.path.join(BASE_DIR, "data", "cleaned_full_data.csv")
df = pd.read_csv(data_path)

# === Encode categorical variables ===
label_encoders = {}
for col in df.select_dtypes(include='object').columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# === Scale features ===
features = df.drop('y', axis=1)
target = df['y']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# === Train/test split ===
X_train, X_test, y_train, y_test = train_test_split(X_scaled, target, test_size=0.2, random_state=42)

# === Train model ===
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)

# === Save files ===
model_dir = os.path.join(BASE_DIR, "models", "decision_tree")
scaler_dir = os.path.join(BASE_DIR, "models", "logistic_regression")
os.makedirs(model_dir, exist_ok=True)
os.makedirs(scaler_dir, exist_ok=True)

joblib.dump(dt_model, os.path.join(model_dir, "model_dt.pkl"))
pickle.dump(scaler, open(os.path.join(scaler_dir, "scaler_dt.pkl"), "wb"))
pickle.dump(label_encoders, open(os.path.join(model_dir, "label_encoder_dt.pkl"), "wb"))

print("✅ Decision Tree model, scaler, and encoders saved successfully.")
