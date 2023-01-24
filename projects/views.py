from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from projects.models import Project
from projects.forms import CreateForm
# Create your views here.

@login_required
def projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "projects": projects,
    }
    return render(request, "projects/list.html", context)

@login_required
def show_project(request, id):
    details = Project.objects.get(id=id)
    context = {
        "details": details
    }
    return render(request, "projects/details.html", context)

@login_required
def create_project(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            create= form.save(False)
            create.owner = request.user
            create.save()
            return redirect("list_projects")
    else:
        form = CreateForm()
    context = {
        "form": form
    }
    return render(request, "projects/create.html", context)
