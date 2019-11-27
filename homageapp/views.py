from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Project,Profile

# Create your views here.
def index(request):
    projects = Project.get_projects()
    return render(request,'index.html',{"projects":projects})