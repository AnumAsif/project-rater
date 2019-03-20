from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Project, Rating, Language

class SignUpForm(UserCreationForm):
    email=forms.EmailField(max_length=254, help_text="Required")
    class Meta:
        model=User
        fields=('email', 'username', 'password1','password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user']
        fields=('bio','contact_no','profile_pic')
        

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        exclude=['post_date','user']
        fields=('title','description','link','languages','image',)
        widgets={
            'title':forms.TextInput(attrs={'placeholder':'Enter Project Title'}) ,
            'description':forms.Textarea(attrs={'placeholder':'Enter Project Description'}),
            'link':forms.URLInput(attrs={'placeholder':'Enter link to live site...'}),
        
        }
    # def __init__ (self, *args, **kwargs):
    #     # brand = kwargs.pop("brand")
    #     super(ProjectForm, self).__init__(*args, **kwargs)
    #     self.fields["languages"].widget = forms.widgets.CheckboxSelectMultiple()
    #     self.fields["languages"].help_text = ""
    #     self.fields["languages"].queryset = Language.objects.all()         

class RateForm(forms.ModelForm):
    RATINGS = (
      (1,''),
      (2,''),
      (3,''),
      (4,''),
      (5,''),
      (6,''),
      (7,''),
      (8,''),
      (9,''),
      (10,'')
   )

    design = forms.ChoiceField(choices=RATINGS, widget=forms.RadioSelect())
    usability = forms.ChoiceField(choices=RATINGS, widget=forms.RadioSelect())
    content = forms.ChoiceField(choices=RATINGS, widget=forms.RadioSelect())  
    class Meta:
            model=Rating
            exclude=['user','project']
            fields=('design','usability','content')                    

class languageForm(forms.ModelForm):
    class Meta:
        model=Language
        fields=('title',)        