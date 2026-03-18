from django.urls import path
from . import views

urlpatterns = [
   path("electronics/",views.RegistrationForm,name="elect"),
   path("output/",views.result,name="price"),
   path("register/",views.registerForm,name="dummy"),
]
