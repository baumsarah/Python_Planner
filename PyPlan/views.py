from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "PyPlan/index.html")

def sarah(request):
    return HttpResponse("Hello, Sarah!")

def greet(request, name):
    return render(request, "PyPlan/greet.html", {
        "name": name.capitalize()
    })
