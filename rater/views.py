from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Project
# Create your views here.
def index(request):
    projects=Project.get_all_projects()
    
    return render(request, 'index.html', {"projects":projects})

