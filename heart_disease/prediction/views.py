from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HeartDiseaseInputSerializer
import joblib
import pandas as pd
import os
from django.conf import settings

# Create your views here.
class PredictAPIView(APIView):
    """
    POST /api/predict/
    {
      "age":63, "sex":1, "cp":3, "trestbps":145, "chol":233,
      "fbs":1, "restecg":0, "thalach":150, "exang":0,
      "oldpeak":2.3, "slope":0, "ca":0, "thal":1
    }
    => { "prediction": 1 }
    """
    def post(self, request):
        serializer = HeartDiseaseInputSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        model = joblib.load(os.path.join(settings.BASE_DIR, 'models', 'best_heart_disease_model.joblib'))
        scaler = joblib.load(os.path.join(settings.BASE_DIR, 'models', 'feature_scaler.joblib'))

        # Chuyển đổi dữ liệu đầu vào thành DataFrame
        input_data = pd.DataFrame([serializer.validated_data])
        # Chuẩn hóa dữ liệu
        input_data_scaled = scaler.transform(input_data)
        # Dự đoán
        pred = model.predict(input_data_scaled)[0]
        # Trả về kết quả dự đoán

        return Response({'prediction': pred})