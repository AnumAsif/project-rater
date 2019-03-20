from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Project, Profile, Language
from django.http import JsonResponse
from .forms import ProjectForm, SignUpForm, ProfileForm
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

# def edit_profile(request):
#     if request.method == 'POST':
#         # user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if profile_form.is_valid():
#             # user_form.save()
#             profile_form.save(commit=False)
#             profile_form.user=request.user
#             profile_form.save()
#             messages.success(request, _('Your profile was successfully updated!'))
#             return redirect('edit_profile')
#         else:
#             messages.error(request, _('Please correct the error below.'))
#     else:
#         # user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request,'edit_profile.html', {'profile_form': profile_form } )