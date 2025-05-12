import os, joblib
from django.conf import settings
import numpy as np

# Đường dẫn đến model & scaler
MODEL_PATH  = './heart_disease/models/svm_model.pkl'
SCALER_PATH = './heart_disease/models/scaler.pkl'

# Load 1 lần ở module import
_model  = joblib.load(MODEL_PATH)
_scaler = joblib.load(SCALER_PATH)

def predict_heart_disease(data: dict) -> int:
    """
    data: dict với các key:
      'age','sex','cp','trestbps','chol','fbs',
      'restecg','thalach','exang','oldpeak','slope','ca','thal'
    Trả về 0 hoặc 1.
    """
    # Lấy thứ tự features đúng
    feature_order = [
        'age','sex','cp','trestbps','chol','fbs',
        'restecg','thalach','exang','oldpeak','slope','ca','thal'
    ]
    x = np.array([data[f] for f in feature_order], dtype=float).reshape(1, -1)
    x_scaled = _scaler.transform(x)
    return int(_model.predict(x_scaled)[0])
