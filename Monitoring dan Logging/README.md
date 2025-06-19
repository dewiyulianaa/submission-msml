# 📡 Monitoring dan Logging - Proyek Akhir MSML

Folder ini berisi seluruh bukti konfigurasi dan implementasi sistem monitoring dan alerting untuk model machine learning yang telah disajikan.

---

## 1. 📤 Serving Model

Model machine learning disajikan sebagai REST API menggunakan Flask. Endpoint utama untuk inference adalah:

POST http://localhost:8000/predict

### 🔹 File terkait:
- `7.Inference.py`: untuk mengirim data dummy ke endpoint dan mencatat waktu inferensi.
- Model telah diekspos dengan Prometheus client melalui route `/metrics`.

---

## 2. 📈 Monitoring dengan Prometheus dan Grafana

### 🔧 Konfigurasi Prometheus
Prometheus dikonfigurasi untuk men-scrape metrik dari model pada port 8000.

- File konfigurasi:
  - `2.prometheus.yml` → konfigurasi scrape target `localhost:8000`
- File exporter:
  - `3.prometheus_exporter.py` → mencatat metrik waktu prediksi (`prediction_time_seconds_sum`)

### 🖼️ Bukti:
- `4.bukti monitoring Prometheus/` → tangkapan layar query metrik di Prometheus UI
- `5.bukti monitoring Grafana/` → tampilan panel time-series di Grafana untuk metrik tersebut

---

## 3. 🚨 Alerting di Grafana

### 🔔 Rule Alerting
Sebuah rule alert telah dibuat di Grafana untuk memantau metrik `prediction_time_seconds_sum`.

- Nama alert: `Alert_Prediction_Time`
- Trigger: jika nilai `prediction_time_seconds_sum` melebihi **3**
- Status saat aktif: **Firing**
- Evaluasi setiap: 1 menit
- Mode evaluasi: Strict

### 📬 Contact Point
Alert telah dikonfigurasikan untuk mengirim notifikasi ke alamat email:

dewiyulianaa938@gmail.com

via metode: **Email**

### 🖼️ Bukti:
- `6.bukti alerting Grafana/` → tangkapan layar rule alert aktif (firing) dan panel metrik
- File YAML ekspor: `modify-export-Prediction Alert Group.yaml`

---

## 4. 🧪 Pengujian Inference

File `7.Inference.py` digunakan untuk mengirim permintaan ke model dan menghasilkan metrik yang dapat dimonitor dan dijadikan dasar alerting.

---

## ✅ Ringkasan File

| No | Nama File                          | Deskripsi |
|----|------------------------------------|-----------|
| 1  | `2.prometheus.yml`                | Konfigurasi Prometheus |
| 2  | `3.prometheus_exporter.py`        | Prometheus client metrics |
| 3  | `4.bukti monitoring Prometheus/`  | Screenshot Prometheus |
| 4  | `5.bukti monitoring Grafana/`     | Screenshot visualisasi metrik |
| 5  | `6.bukti alerting Grafana/`       | Screenshot & YAML alert |
| 6  | `7.Inference.py`                  | Script uji endpoint |
| 7  | `modify-export-Prediction Alert Group.yaml` | Backup rule alert |

---

📌 Semua konfigurasi telah berjalan dengan baik secara lokal, dan seluruh metrik serta alerting tervalidasi melalui Prometheus dan Grafana.

