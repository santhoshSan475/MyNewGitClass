from django.shortcuts import render,redirect

from .models import StudentModel
from .forms import StudentForm
from django.http import HttpResponse
# Create your views here.

#GET - retrieving data
def studentTable(request):
    studentValue = StudentModel.objects.all()
    return render(request,"crudApp/studentData.html",{"studentValue":studentValue})

#POST - Creating Data
def studentRegistration(request):
    if request.method == "POST":
        form = StudentForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect("Data")
        else:
            return HttpResponse("<h3>Invalid</h3>")
        
    form = StudentForm
    return render(request,"crudApp/input.html",{"form":form})


#PUT - Updating data

def UpdatingStudentTable(request,id):
    data = StudentModel.objects.get(id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect("Data")
        else:
            return HttpResponse("<h3>Invalid</h3>")

    form = StudentForm
    return render(request,"crudApp/input.html",{"form":form})



#Delete - deleting Data

def DeleteStudentTable(request,id):
    data = StudentModel.objects.get(id=id)
    data.delete()
    return redirect('Data')




