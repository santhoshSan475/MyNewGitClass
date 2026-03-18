from django.shortcuts import render

# Create your views here.

def indexContent(request):
    context = {
        "title":"IndexPage",
        "feature1":"Fast Development",
        "feature2":"Secure by Default",
        "feature3":"powerful Backend"
    }
    return render(request,"templateApp/index.html",context)


def aboutContent(request):
    return render(request,"templateApp/about.html")


