from django.shortcuts import render,redirect
import requests

def medicalInfo(request):
    url = 'http://127.0.0.1:8000/api/v3/patient/'
    response = requests.get(url)
    data = response.json()
    return render(request,'medicalApp/Table.html',{"patient":data})



def updateMedicalInfo(request,id):
    pass



def deleteMedicalInfo(request,id):
    url = f'http://127.0.0.1:8000/api/v3/patient/{id}/'
    requests.delete(url)
    return redirect("registration")





