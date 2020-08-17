from django.urls import path # gives us the ability to reroute URLs
from . import views # imports any functions we've created in views.py

app_name = "PyPlan"
urlpatterns = [
    path("", views.index, name="index"),
    path("Sarah", views.sarah, name="Sarah"),
    path("<str:name>", views.greet, name="greet")
]