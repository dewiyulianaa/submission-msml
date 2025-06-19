import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib

# Load data
X = pd.read_csv("membangun model\X_final.csv")
y = pd.read_csv("membangun model\y_final.csv")

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# MLflow setup
mlflow.set_experiment("Tuning Logistic Regression")

with mlflow.start_run():
    # Define model and parameter grid
    model = LogisticRegression(solver='liblinear', random_state=42)
    param_grid = {
        'C': [0.01, 0.1, 1.0, 10.0],  # regularisasi
        'penalty': ['l1', 'l2']
    }

    # Grid search
    grid = GridSearchCV(model, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
    grid.fit(X_train, y_train.values.ravel())

    best_model = grid.best_estimator_
    y_pred = best_model.predict(X_test)

    # Metrics
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    # MLflow logging
    mlflow.log_params(grid.best_params_)
    mlflow.log_metric("accuracy", acc)
    mlflow.log_metric("precision", prec)
    mlflow.log_metric("recall", rec)
    mlflow.log_metric("f1_score", f1)
    mlflow.sklearn.log_model(best_model, "logreg_tuned_model")

    # Simpan lokal juga
    joblib.dump(best_model, "best_logreg_model.pkl")

    print("Best Params:", grid.best_params_)
    print("Accuracy:", acc)
