from rest_framework import serializers

class HeartDiseaseInputSerializer(serializers.Serializer):
    age      = serializers.IntegerField()
    sex      = serializers.ChoiceField(choices=[(0,0),(1,1)])
    cp       = serializers.IntegerField()
    trestbps = serializers.IntegerField()
    chol     = serializers.IntegerField()
    fbs      = serializers.ChoiceField(choices=[(0,0),(1,1)])
    restecg  = serializers.IntegerField()
    thalach  = serializers.IntegerField()
    exang    = serializers.ChoiceField(choices=[(0,0),(1,1)])
    oldpeak  = serializers.FloatField()
    slope    = serializers.IntegerField()
    ca       = serializers.IntegerField()
    thal     = serializers.IntegerField()