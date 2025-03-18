from django.shortcuts import render
from .forms import GroupForm, ProcessForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import PGroup

# Create your views here.
def index(request):
    grps = PGroup.objects.all()
    return render(request,"manageprocess/index.html", {"groups": grps} )

def add_group(request):
    if request.method == "POST":
        gf = GroupForm(request.POST)
        if gf.is_valid():
            # grp = PGroup(group_name=gf.cleaned_data['group_name'])
            # grp.save()
            # print(gf.cleaned_data)
            gf.save()
            return HttpResponseRedirect(reverse("process:successf"))

    else:
        gf = GroupForm()
    return render(request, "manageprocess/form_data.html", {"form":gf})

def success_form_submit(request):
    return render(request,"manageprocess/thankyou.html")

def login(request):
    return HttpResponse("Login")

def add_process(request, group_name):
    if request.method == "POST":
        pf = ProcessForm(request.POST)
        if pf.is_valid():
            pf.save()
            return HttpResponseRedirect(reverse("process:index"))
    else:
        pf = ProcessForm()
    return render(request, "manageprocess/add_process.html", {"form":pf})