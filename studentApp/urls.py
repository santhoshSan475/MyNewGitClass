from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("studentsInfo",views.studentObjectInfoView,basename="std")

urlpatterns = [
    path("",include(router.urls))
]



