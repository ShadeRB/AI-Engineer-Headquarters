import joblib
import pandas as pd
from evaluation import evaluate_model, predict_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# === Load and encode dataset ===
data_path = r"C:\Users\ritup\Documents\DataScience\bank_marketing_ml\data\cleaned_full_data.csv"
df = pd.read_csv(data_path)

label_encoder_dt = joblib.load('bank_marketing_ml/models/decision_tree/label_encoder_dt.pkl')
label_encoder_rf = joblib.load('bank_marketing_ml/models/random_forest/label_encoder_rf.pkl')

for col, encoder in label_encoder_dt.items():
    if col in df.columns:
        df[col] = encoder.transform(df[col])

X = df.drop('y', axis=1)
y = df['y']
_, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# === Evaluate Decision Tree ===
model_dt = joblib.load('bank_marketing_ml/models/decision_tree/model_dt.pkl')
y_pred_dt = predict_model(model_dt, X_test)

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

dt_results = {
    "Accuracy": accuracy_score(y_test, y_pred_dt),
    "Precision": precision_score(y_test, y_pred_dt),
    "Recall": recall_score(y_test, y_pred_dt),
    "F1 Score": f1_score(y_test, y_pred_dt),
}

# 🔽 ADD THIS LINE HERE
evaluate_model(y_test, y_pred_dt, model_name="Decision Tree")

# === Evaluate Random Forest ===
# === Evaluate Random Forest ===
model_rf = joblib.load('bank_marketing_ml/models/random_forest/model_rf.pkl')
y_pred_rf = predict_model(model_rf, X_test)

rf_results = {
    "Accuracy": accuracy_score(y_test, y_pred_rf),
    "Precision": precision_score(y_test, y_pred_rf),
    "Recall": recall_score(y_test, y_pred_rf),
    "F1 Score": f1_score(y_test, y_pred_rf),
}

# 🔽 ADD THIS LINE HERE
evaluate_model(y_test, y_pred_rf, model_name="Random Forest")
 
# === Print Pretty Summary ===
def format_percent(x):
    return f"{x * 100:.2f}%"

print("\n📊 Evaluation Summary: Bank Marketing Campaign\n")

print("🌳 Decision Tree")
print("----------------")
for metric, value in dt_results.items():
    print(f"✔️ {metric:<9}: {format_percent(value)}")
print("⚠️ Comment  : High false positive rate; not great at capturing \"yes\" (subscribers)\n")

print("🌲 Random Forest")
print("----------------")
for metric, value in rf_results.items():
    print(f"✔️ {metric:<9}: {format_percent(value)}")
print("💡 Comment  : Better precision/recall trade-off — preferred for this classification task.\n")

# === Plot the comparison chart ===
metrics = list(dt_results.keys())
dt_scores = list(dt_results.values())
rf_scores = list(rf_results.values())

x = range(len(metrics))
bar_width = 0.35

plt.figure(figsize=(8, 5))
plt.bar(x, dt_scores, width=bar_width, label='Decision Tree', color='lightgreen')
plt.bar([i + bar_width for i in x], rf_scores, width=bar_width, label='Random Forest', color='skyblue')

plt.xticks([i + bar_width / 2 for i in x], metrics)
plt.ylabel('Score')
plt.title('Model Evaluation Comparison')
plt.ylim(0, 1)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
