from django.shortcuts import render
from .forms import GroupForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,"manageprocess/index.html")

def form_render(request):
    if request.method == "POST":
        gf = GroupForm(request.POST)
        if gf.is_valid():
            print(gf.cleaned_data)
            return HttpResponseRedirect(reverse("process:successf"))

    else:
        gf = GroupForm()
    return render(request, "manageprocess/form_data.html", {"form":gf})

def success_form_submit(request):
    return render(request,"manageprocess/index.html")
