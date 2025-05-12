import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_and_preprocess(path='./svm_model/heart_disease_data.csv'):
    # 1. Đọc data
    df = pd.read_csv(path)

    # 2. Label encode 'thal' (shift 1–3 → 0–2)
    le = LabelEncoder()
    df['thal'] = le.fit_transform(df['thal'])

    # 3. X, y
    X = df.drop('target', axis=1)
    y = df['target']

    # 4. Scale
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, scaler, X.columns