import pandas as pd
from sklearn.model_selection import train_test_split

# Load dataset asli
df = pd.read_csv("membangun model\HR_preprocessing\WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Drop target untuk X
X = df.drop(columns=["Attrition"])
y = df["Attrition"]

# Split ulang (gunakan random_state sama seperti saat training)
X_train, X_test_raw, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Simpan X_test mentah (yang dibutuhkan inference)
X_test_raw.to_csv("X_test_raw.csv", index=False)

print("Berhasil menyimpan X_test_raw.csv")
