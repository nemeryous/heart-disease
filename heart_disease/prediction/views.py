from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HeartDiseaseInputSerializer
import joblib
import pandas as pd
import os
from django.conf import settings

class PredictAPIView(APIView):
    def post(self, request):
        serializer = HeartDiseaseInputSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        model = joblib.load(os.path.join(settings.BASE_DIR, 'models', 'best_heart_disease_model.joblib'))
        scaler = joblib.load(os.path.join(settings.BASE_DIR, 'models', 'feature_scaler.joblib'))

        input_data = pd.DataFrame([serializer.validated_data])
        input_data_scaled = scaler.transform(input_data)
        pred = model.predict(input_data_scaled)[0]
        
        prob = model.predict_proba(input_data_scaled)[0]
        
        probability_heart_disease = prob[1]
        
        if pred == 1:
            confidence = round(probability_heart_disease * 100, 2)
        else:
            confidence = round(prob[0] * 100, 2)
            
        return Response({
            'prediction': int(pred),
            'confidence': f"{confidence}%"
        })