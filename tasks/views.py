from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tasks.forms import CreateTaskForm
from tasks.models import Task

# Create your views here.
@login_required
def create_task(request):
    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form = form.save()
            return redirect("list_projects")
    else:
        form = CreateTaskForm()
    context = {
        "form": form,
        }
    return render(request, "tasks/create.html", context)


@login_required
def show_my_tasks(request):
    mine = Task.objects.filter(assignee=request.user)
    context = {
        "mine": mine,
    }
    return render(request, "tasks/detail.html", context)
