from django.urls import path
from . import views

urlpatterns = [
    path("student/",views.studentTable,name="Data"),
    path("registerForm/",views.studentRegistration,name="registration"),
    path("updateStudent/<int:id>/",views.UpdatingStudentTable, name="UpdateTable"),
    path("deleteStudent/<int:id>/",views.DeleteStudentTable, name="deleteTable")
]