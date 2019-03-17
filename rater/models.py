from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Profile(models.Model):
    '''
    Add additional fields for django user
    '''
    user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    username=models.CharField(max_length=50)
    profile_pic=ImageField(blank=True, manual_crop='800x800')
    bio=HTMLField()
    contact_no=models.IntegerField(max_length=12)

    def __str__(self):
        return self.username

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