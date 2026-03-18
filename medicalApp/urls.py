from django.urls import path
from . import views
urlpatterns = [
   path("patient/",views.medicalObjectInfo.as_view()),
   path("patient/<int:id>/",views.medicalObjectUpdateInfo.as_view())
]