from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse

# Create your views here.
def index(request):

    # Check if there already exists a "planners" key in our session
    if "planners" not in request.session:

        # If not, create a new list of planners
        request.session["planners"] = []

    return render(request, "PyPlan/index.html", {
        "planners": request.session["planners"]
    })

# Add a new planner
def add(request):

    # Check if method is POST
    if request.method == "POST":

        # Take in the data the user submitted and save it as a form
        form = NewPlannerForm(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the planner from the 'cleaned' version of form data
            planner = form.cleaned_data["planner"]

            # Add the new planner to our list of planners
            request.session["planners"] += [planner]

            # Redirect user to list of planners
            return HttpResponseRedirect(reverse("PyPlan:index"))

        else:

            # If the form is invalid, re-render the page with existing information
            return render(request, "PyPlan/add.html", {
                "form": form
            })
    return render(request, "PyPlan/add.html", {
        "planner": NewPlannerForm()
    })

class NewPlannerForm(forms.Form):
    planner = forms.CharField(label="")