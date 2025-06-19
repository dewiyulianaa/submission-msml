import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Aktifkan autolog
mlflow.autolog()

# Load data
X = pd.read_csv("https://raw.githubusercontent.com/dewiyulianaa/submission-msml/main/membangun_model/HR_preprocessing/X_final.csv")
y = pd.read_csv("https://raw.githubusercontent.com/dewiyulianaa/submission-msml/main/membangun_model/HR_preprocessing/y_final.csv")
y = y.values.ravel()

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train model — TIDAK PERLU `with mlflow.start_run()`
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluasi hasil (MLflow autolog akan otomatis mencatat)
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(f"Precision: {precision_score(y_test, y_pred)}")
print(f"Recall: {recall_score(y_test, y_pred)}")
print(f"F1 Score: {f1_score(y_test, y_pred)}")
