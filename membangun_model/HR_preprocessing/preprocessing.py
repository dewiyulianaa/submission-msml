# preprocessing.py

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def preprocess(path_csv):
    """
    Melakukan preprocessing pada data karyawan.
    Argumen:
        path_csv (str): path ke file CSV.
    Return:
        X (pd.DataFrame): fitur akhir hasil preprocessing.
        y (pd.Series): target (Attrition).
    """
    df = pd.read_csv(path_csv)

    # Drop kolom yang tidak relevan
    df.drop(columns=['EmployeeCount', 'EmployeeNumber', 'Over18', 'StandardHours'], inplace=True)

    # Hapus duplikat
    df.drop_duplicates(inplace=True)

    # Ubah kolom target menjadi numerik
    df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})

    # One-hot encoding untuk kolom kategorikal
    categorical_cols = df.select_dtypes(include='object').columns.tolist()
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    # Pisahkan fitur dan target
    X = df.drop(columns='Attrition')
    y = df['Attrition']

    # Scaling numerik
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Konversi ke DataFrame kembali
    X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

    return X_scaled, y
