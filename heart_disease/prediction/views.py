from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HeartDiseaseInputSerializer
from .services.model_service import predict_heart_disease
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

        pred = predict_heart_disease(serializer.validated_data)
        return Response({'prediction': pred})