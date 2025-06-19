import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib

# Aktifkan autolog agar MLflow otomatis log semua metrik, parameter, dan artefak
mlflow.autolog()

# Load dataset
X = pd.read_csv("https://raw.githubusercontent.com/dewiyulianaa/submission-msml/main/membangun_model/HR_preprocessing/X_final.csv")
y = pd.read_csv("https://raw.githubusercontent.com/dewiyulianaa/submission-msml/main/membangun_model/HR_preprocessing/y_final.csv")
y = y.values.ravel()  # ubah ke bentuk array 1 dimensi

# Split data (stratify biar distribusi target sama)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Set experiment
mlflow.set_experiment("Tuning Logistic Regression")

with mlflow.start_run():
    # Definisikan model dasar dan hyperparameter
    model = LogisticRegression(solver='liblinear', random_state=42)
    param_grid = {
        'C': [0.01, 0.1, 1.0, 10.0],
        'penalty': ['l1', 'l2']
    }

    # Grid search
    grid = GridSearchCV(model, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
    grid.fit(X_train, y_train)

    # Evaluasi
    best_model = grid.best_estimator_
    y_pred = best_model.predict(X_test)

    print("Best Params:", grid.best_params_)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Precision:", precision_score(y_test, y_pred))
    print("Recall:", recall_score(y_test, y_pred))
    print("F1 Score:", f1_score(y_test, y_pred))

    # Simpan model terbaik ke file lokal (optional)
    joblib.dump(best_model, "best_logreg_model.pkl")
