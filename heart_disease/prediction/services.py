# prediction/services/model_service.py

import os, joblib
from django.conf import settings
import numpy as np

# 1. Đường dẫn đến pipeline.pkl
PIPELINE_PATH = os.path.join(settings.BASE_DIR, 'models', 'svm_pipeline.pkl')

# 2. Load pipeline 1 lần khi import module
_pipeline = joblib.load(PIPELINE_PATH)

def predict_heart_disease(data: dict) -> int:
    """
    data: dict với các key:
      'age','sex','cp','trestbps','chol','fbs',
      'restecg','thalach','exang','oldpeak','slope','ca','thal'
    Trả về 0 hoặc 1.
    """
    feature_order = [
        'age','sex','cp','trestbps','chol','fbs',
        'restecg','thalach','exang','oldpeak','slope','ca','thal'
    ]
    # 3. Chuyển dict → array đúng thứ tự
    x = np.array([data[f] for f in feature_order], dtype=float).reshape(1, -1)

    # 4. Pipeline sẽ tự scale và predict
    pred = _pipeline.predict(x)

    return int(pred[0])