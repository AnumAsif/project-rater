from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Project, Rating
from django.db import models
# Create your tests here.
class ProfileTestCase(TestCase):
    def setUp(self):
        self.u1 = User.objects.create(username='user1')
        self.anum = Profile.objects.create(user=self.u1)

    def tearDown(self):
        self.anum.delete()
        self.u1.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.anum, Profile))

    def test_save_profile(self):
        self.anum.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_search_profile(self):
        self.anum.save_profile()
        profile= Profile.search_profile(self.anum)
        self.assertTrue(len(profile)>0)

    def test_get_by_id(self):
        self.anum.save_profile()
        profile=Profile.get_by_id(self.anum)
        self.assertTrue(profile!=None)


class ImageTestCase(TestCase):

    def setUp(self):
        self.u1 = User.objects.create(username='user1')
        self.project=Project.objects.create(title="portfolio",description="dasdasdasd", user=self.u1)        

    def tearDown(self):
        self.project.delete()
        self.u1.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))

    def test_save_project(self):
        self.project.save_project()
        projects=Project.objects.all()
        self.assertTrue(len(projects)>0)
     
    def test_get_all_projects(self):
        self.project.save_project()
        projects= Project.get_all_projects()
        self.assertTrue(len(projects)>0)

class RatingTestCase(TestCase):

        
    def setUp(self):   
        self.u1 = User.objects.create(username='user1')
        self.project=Project.objects.create(title="portfolio",description="dasdasdasd", user=self.u1)        
        self.rating=Rating.objects.create(user=self.u1, project=self.project, design = 5, usability = 5, content = 5)

    def tearDown(self):
        self.rating.delete()    
        self.project.delete()
        self.u1.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rating))

    
    def test_save_rating(self):
        self.rating.save_rate()
        ratings=Rating.objects.all()
        self.assertTrue(len(ratings)>0)

    def test_get_ratings_by_projects(self):
        self.project.save_project()
        self.rating.save_rate()
        ratings=Rating.get_ratings_by_project(self.project.id)
        self.assertTrue(len(ratings)>0)