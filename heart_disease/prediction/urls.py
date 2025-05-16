from django.urls import path
from .views import *

urlpatterns = [
    path('predict/', PredictAPIView.as_view(), name='predict')
]