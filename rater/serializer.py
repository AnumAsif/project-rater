from rest_framework import serializers
from .models import Profile,Project,Language
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
   
   class Meta:
        model = Profile
        fields = ['bio','contact_no','profile_pic']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer('profile')
    class Meta:
        model = User
        fields = ['username','email','profile']
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['title']

class  ProjectSerializer(serializers.ModelSerializer):
   user = UserSerializer('profile')
   languages = LanguageSerializer('language',many=True)
   class Meta:
      model = Project
      fields = ['title','description','languages','link','user','image']