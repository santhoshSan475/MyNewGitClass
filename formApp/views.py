from django.shortcuts import render
from .forms import dummyForm
# Create your views here.


def RegistrationForm(request):
    return render(request,"formApp/Electronics.html")

def result(request):
    Laptop = int(request.GET.get("Laptop"))
    Mobiles = int(request.GET.get("mobiles"))
    Fridge = int(request.GET.get("fridge"))
    Television = int(request.GET.get("television"))
    Headphones = int(request.GET.get("headphones"))
    smartwatch = int(request.GET.get("smartwatch"))
    Total = Laptop + Mobiles + Fridge + Television + Headphones + smartwatch

    return render(request,"formApp/Total.html",{"total":Total})



def registerForm(request):
    form = dummyForm
    return render(request,"formApp/dummyForm.html",{"form":form})

