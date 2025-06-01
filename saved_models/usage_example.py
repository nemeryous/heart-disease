
# CÁCH SỬ DỤNG MÔ HÌNH ĐÃ LUU
import joblib
import pandas as pd
import numpy as np

# Tải mô hình và scaler
model = joblib.load('saved_models/best_heart_disease_model.joblib')
scaler = joblib.load('saved_models/feature_scaler.joblib')

# Ví dụ dữ liệu mới (thay thế bằng dữ liệu thực tế)
new_data = pd.DataFrame({
    'age': [50],
    'sex': [1],
    'cp': [2],
    'trestbps': [120],
    'chol': [200],
    'fbs': [0],
    'restecg': [1],
    'thalach': [150],
    'exang': [0],
    'oldpeak': [1.0],
    'slope': [2],
    'ca': [0],
    'thal': [2]
})

# Chuẩn hóa dữ liệu
new_data_scaled = scaler.transform(new_data)

# Dự đoán
prediction = model.predict(new_data_scaled)
probability = model.predict_proba(new_data_scaled)

print(f"Dự đoán: {prediction[0]} (0: Không có bệnh tim, 1: Có bệnh tim)")
print(f"Xác suất: {probability[0]}")
