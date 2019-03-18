from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Profile(models.Model):
    '''
    Add additional fields for django user
    '''
    user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_pic=ImageField(blank=True, manual_crop='200x200')
    bio=models.TextField(max_length=200)
    contact_no=models.IntegerField(null=True)


    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    @classmethod
    def search_profile(cls, name):
        profile=Profile.objects.filter(user__username__icontains=name)
        return profile 

    @classmethod
    def get_by_id(cls, id):
        profile=Profile.objects.get(user=id)
        return profile 

    @classmethod
    def filter_by_id(cls, id): 
        profile=Profile.objects.filter(user=id).first()
        return profile    

class Project(models.Model):
    '''
    A class containing all the project information
    '''
    title=models.CharField(max_length=50)
    image = ImageField(null=True, manual_crop='1280x720')
    description = models.TextField(max_length=200)
    link = models.URLField(null=True, blank=True, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date=models.DateTimeField(auto_now=True)
 

    class Meta:
        ordering=('-post_date',)

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    @classmethod
    def get_all_projects(cls):
        projects=Project.objects.all()
        return projects

    @classmethod
    def get_project_by_userid(cls, id):
        project=Project.objects.filter(user__pk=id)

class Rating(models.Model):
    '''
    To store average rate given to the project
    '''              
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project= models.ForeignKey(Project, on_delete=models.CASCADE)
    design=models.IntegerField(default=0)
    usability=models.IntegerField(default=0)
    content=models.IntegerField(default=0)
    
    def save_rate(self):
        self.save()
    
    @classmethod
    def get_ratings_by_project(cls, id):
        ratings=Rating.objects.filter(project__id=id)
        return ratings

class Language(models.Model):
    '''
    To add language used to create a project
    '''
    title=models.CharField(max_length=50)
    projects = models.ManyToManyField(Project)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)