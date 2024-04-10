from rest_framework.serializers import ModelSerializer
from .models import *

class videoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class flightSerializer(ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'