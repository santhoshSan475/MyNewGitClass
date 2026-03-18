from django.shortcuts import render
from .models import MedicalInfo
from .serializers import medicalSerializer
from rest_framework import generics
# Create your views here.


class medicalObjectInfo(generics.ListCreateAPIView):
    queryset = MedicalInfo.objects.all()
    serializer_class = medicalSerializer


class medicalObjectUpdateInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalInfo.objects.all()
    serializer_class = medicalSerializer
    lookup_field = "id"
