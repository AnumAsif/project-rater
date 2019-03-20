from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Project, Profile, Language, Rating
from django.http import JsonResponse
from .forms import ProjectForm, SignUpForm, ProfileForm, RateForm
from django.contrib.auth.models import User
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

@login_required(login_url='/login')
def project(request, project_id):
    project=Project.objects.filter(id=project_id).first()
    user=request.user
    rates = Rating.objects.filter(user=user, project=project).first()
    averageRate=(rates.usability+rates.design+rates.content)/3
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid() and rates is None:
            rate=form.save(commit=False)
            rate.user=user
            rate.project=project
            rate.save()
            return redirect('project',project_id=project.id)
        else:
            rates.delete()
            rate=form.save(commit=False)
            rate.user=user
            rate.project=project
            rate.save()
            return redirect('project',project_id=project.id)

    else:
        form = RateForm()
        all_rates = Rating.objects.filter(project=project).all()
        
    # return render(request,'project.html',{'form':form, 'current_user':user,"project":project})
        return render(request, 'project.html',{'project':project,'form':form, 'average':averageRate, 'all_rates':all_rates})

# def rate(request):
#     design_rating = request.POST.get('rating')
#     data = {'success': 'You have been successfully added to mailing list'}
#     return JsonResponse(data)

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

def search(request):
    current_user=request.user
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        projects = Project.objects.filter(title__icontains=search_term).all()
        message=f'{search_term}'

        return render(request, 'search.html', {'message':message, 'projects':projects, 'current_user':current_user})

    else:
        message='Enter term to search'
        return render(request, 'search.html',{'message':message, 'current_user':current_user})     


@login_required(login_url='/login')
def profile(request,username):
    user=User.objects.get(username=username)
    projects=Project.objects.filter(user__pk=user.id)
    current_user = request.user
    return render(request, 'profile.html',{'current_user':current_user,'user':user,'projects':projects})    

@login_required(login_url='/login')
def edit_profile(request):
    user=request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = user
            edit.save()
            return redirect('edit_profile')
    else:
        form = ProfileForm()

    return render(request, 'edit_profile.html', {'form':form, 'current_user':user})

# @login_required(login_url='/login')
# def rate(request, id):
#     project=Project.objects.filter(id=id).first()
#     user=request.user
#     if request.method == 'POST':
#         form = RateForm(request.POST)
#         if form.is_valid():
#             rate=form.save(commit=False)
#             rate.user=user
#             rate.project=project
#             rate.save()
#             return redirect('project',project_id=project.id)
#     else:
#         form = RateForm()
#     return render(request,'project.html',{'form':form, 'current_user':user,"project":project})

