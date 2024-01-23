from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from project.models import Project

from .models import TodoList


def add(request, project_id):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)

    if request.method == "POST":
        name = request.POST.get("name", "")
        description = request.POST.get("description", "")

        if name:
            TodoList.objects.create(
                project=project,
                name=name,
                description=description,
                created_by=request.user,
            )

            return redirect(f"/projects/{project_id}/")

    return render(request, "todolist/add.html")
