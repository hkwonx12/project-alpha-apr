from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from projects.models import Project
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
