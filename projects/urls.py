from django.urls import path
from projects.views import projects, show_project

urlpatterns = [
    path("", projects, name="list_projects"),
    path("<int:id>/", show_project, name="show_project")
    
]
