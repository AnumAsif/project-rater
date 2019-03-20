from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Project, Profile, Language
from django.http import JsonResponse
from .forms import ProjectForm, SignUpForm, ProfileForm
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request,user)
            profile = Profile(user=user)
            profile.save()
            
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html',{"form":form})            

def index(request):
    projects=Project.get_all_projects()
    
    return render(request, 'index.html', {"projects":projects})

def project(request, project_id):
    project=Project.objects.filter(id=project_id).first()

    return render(request, 'project.html',{'project':project})

def rate(request):
    design_rating = request.POST.get('rating')
    data = {'success': 'You have been successfully added to mailing list'}
    return JsonResponse(data)

@login_required(login_url='/login')
def add_project(request):
    projects=Project.get_all_projects()
    user=request.user
    if request.method == 'POST':
        form=ProjectForm(request.POST)
        if form.is_valid():
            project=form.save(commit =False)
            project.user=user
            project.save()
            form.save_m2m()
        return redirect('index')
    else:
        form = ProjectForm() 
    return render(request, "new_project.html", {"form":form})       