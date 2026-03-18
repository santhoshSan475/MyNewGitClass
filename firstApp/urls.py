from django.urls import path
from . import views
urlpatterns = [
    path("",views.welcomePage,name="openScript"),
    path("home/<str:name>/",views.homePage,name="homeScript"),
    path("student/<str:name>/<int:age>/",views.StudentInfo,name="data"),
    path("main/",views.mainPage,name="mainContent"),
    path("content/",views.contentPage,name="conPage"),
    path("about/<str:name>/<int:age>/",views.aboutPage,name="aboutInfo"),
    path("index/<str:name>/<int:age>/",views.indexPage,name="indexLoad")
]