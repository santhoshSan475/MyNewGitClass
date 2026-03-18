from rest_framework import serializers
from .models import MedicalInfo


class medicalSerializer(serializers.ModelSerializer):
   class Meta:
       model = MedicalInfo
       fields = '__all__'