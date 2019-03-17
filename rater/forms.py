from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Project, Rate

class SignUpForm(UserCreationForm):
    email=forms.EmailField(max_length=254, help_text="Required")
    class Meta:
        model=User
        fields=('email', 'username', 'password1','password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user']

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        exclude=['post_date','user']
        widgets={
            'title':forms.TextInput(attrs={'placeholder':'Enter Project Name...'})       }
            'description':forms.Textarea(attrs={'placeholder':'Enter project description...'}),
            'link':forms.URLField(attrs={'placeholder':'Enter project URL'})
        }    

class RateForm(forms.ModelForm):
    class Meta:
        model=Rateexclude=['user','project']
        fields=('design','usability','content')                    