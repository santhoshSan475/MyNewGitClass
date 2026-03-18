from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

def welcomePage(request):
    return HttpResponse("Welcome to Django class")

def homePage(request,name):

    return render(request,"firstApp/homePage.html",{"name":name})


def StudentInfo(request,name,age):
    return HttpResponse(f"Hello, {name} - age : {age}")


def mainPage(request):
    return redirect("conPage")

def contentPage(request):
    return HttpResponse("<h2>This is contentPage</h2>")

def aboutPage(request,name,age):
    person = {
        "name":name,
        "age":age,
        "gender":"female",
        "qualification":"B TECH",
        "title":"studentInfo"
    }
    return render(request,"firstApp/aboutPage.html",person)


def indexPage(request,name,age):
    return redirect("aboutInfo",name=name,age=age)








