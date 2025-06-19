from prometheus_client import start_http_server, Summary
import random
import time

# Metrik: waktu proses prediksi
PREDICTION_TIME = Summary('prediction_time_seconds', 'Time spent on prediction')

@PREDICTION_TIME.time()
def predict():
    time.sleep(random.uniform(0.1, 0.5))  # simulasi prediksi

if __name__ == '__main__':
    # Menjalankan server di port 8000
    start_http_server(8000)
    print("Exporter berjalan di http://localhost:8000/metrics")
    
    while True:
        predict()
