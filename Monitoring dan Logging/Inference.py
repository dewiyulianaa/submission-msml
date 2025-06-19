import mlflow.sklearn
import pandas as pd

# Ganti dengan path sesuai tracking run milikmu
logged_model = "runs:/8424a6f9c67d47098a69ba9bd8138e31/logistic_model"

# Load model dari MLflow
model = mlflow.sklearn.load_model(logged_model)

# Load data
X_test = pd.read_csv(r"Monitoring dan Logging\X_test_raw.csv")
print("Kolom pada X_final.csv:", X_test.columns.tolist())

# Prediksi
predictions = model.predict(X_test)

# Simpan hasil prediksi ke dalam file CSV

# Buat DataFrame hasil
df_output = pd.DataFrame({
    'EmployeeNumber': X_test['EmployeeNumber'],  # Jika ada kolom identitas
    'Prediction': predictions
})

# Simpan ke CSV
df_output.to_csv('Monitoring dan Logging/hasil_prediksi.csv', index=False)

print("Hasil prediksi berhasil disimpan ke 'hasil_prediksi.csv'")


# Cetak hasil
print("Hasil Prediksi:")
print(predictions)
