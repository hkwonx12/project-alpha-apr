from django.forms import ModelForm
from .models import Project


class CreateForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "description",
            "owner",
        ]
