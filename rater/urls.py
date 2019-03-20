from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
     url(r'^$', views.index, name = 'index'),
     url(r'^signup/$',views.signup, name='signup'),
     url(r'^project/(?P<project_id>\d+)', views.project, name = 'project'),
     # url(r'^rate/(?P<project_id>\d+)', views.rate, name = 'rate'),
     url(r'^login/$',auth_views.login, name="login"),
     # url(r'^ajax/project/(?P<project_id>\d+)', views.rate,name='rate')     
     url(r'^project/$', views.add_project, name="add_project"),
     url(r'^search/', views.search, name="search"),
     url(r'profile/(?P<username>\w+)', views.profile, name='profile'),  
     url(r'^edit/',views.edit_profile, name='edit_profile'),  

]

if settings.DEBUG:
   urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

