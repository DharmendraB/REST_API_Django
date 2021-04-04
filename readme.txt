REST API


//Create project and App Run this code
>> django-admin startproject REST_API_APPS
>> django-admin startapp learn

//install REST_API in django project
>> pip install djangorestframework

//For login authenticate run command
>> pip install djangorestframework-jwt

//Create myserlizer.py file


//Settins.py file code 
INSTALLED_APPS = [
    'learn.apps.LearnConfig',
    ......................
    ......................
        'rest_framework',
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',    
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',        
    ],
# User Authentication requirements Must use this code    
    #    'DEFAULT_AUTHENTICATION_CLASSES': (
    #         'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    #         'rest_framework.authentication.SessionAuthentication',
    #     ),
# No User Authentication requirements this code use
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
# Per page post Display settings
    'PAGE_SIZE': 2
}


//myserlizer.py file Code 
from rest_framework import serializers
from learn.models import Branch, Notice
class BranchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"     

class NoticeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notice
        fields = "__all__"

//Models.py File Code
from django.db import models
from django.db.models.deletion import CASCADE
# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=50)
    hod = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Notice(models.Model):
    subject = models.CharField(max_length=500)
    msg = models.TextField()
    pub_date = models.DateField(auto_now_add=False)
    branch = models.ForeignKey(to=Branch, on_delete=CASCADE, null=True, blank=True)
    
>> python manage.py makemigrations
 >> python manage.py migrate   

//View.py File Code 
from django.views.generic import TemplateView
from learn.models import Branch, Notice
from django.db.models import Q
from rest_framework import viewsets
from learn.myserializer import BranchSerializer, NoticeSerializer
# Create your views here.
class HomeView(TemplateView):
    template_name = "learn/home.html"
    
class AboutView(TemplateView):
    template_name = "learn/about.html"

class ContactView(TemplateView):
    template_name = "learn/contact.html"

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all().order_by("-id")
    serializer_class = BranchSerializer

class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all().order_by("-id")
    serializer_class = NoticeSerializer
    def get_queryset(self):
        search = self.request.GET.get('uq')
        if search == None:
            search =""
        return Notice.objects.filter(Q(subject__icontains = search) | 
        Q(msg__icontains = search)).order_by("-id")

//Main urls.py file code (REST_API_APPS/urls.py)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('learn/', include('learn.urls')),
    path('', RedirectView.as_view(url="learn/")),      
]

// app urls.py file code(learn/urls.py)

from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic.base import RedirectView
from learn import views
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter()
router.register(r'branch',views.BranchViewSet)
router.register(r'notice',views.NoticeViewSet)


urlpatterns = [
     path('home/', views.HomeView.as_view()),
     path('about/', views.AboutView.as_view()),
     path('contact/', views.ContactView.as_view()),
     path('', RedirectView.as_view(url="home/")),
     path(r'api/', include(router.urls)),
     path(r'api-token-auth/', obtain_jwt_token),

]
>> python manage.py runserver 


http://127.0.0.1:8000/learn/api/branch/
http://127.0.0.1:8000/learn/api/notice/
http://127.0.0.1:8000/learn/api/notice/1/

