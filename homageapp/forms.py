from django import forms
from .models import Project


class NewProjectForm(forms.ModelForm):
    live_site = forms.CharField()
    class Meta:
        model = Project
        fields = ("title", "description", "img", "live_site",)