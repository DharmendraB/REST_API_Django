# Required namepace
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic.base import RedirectView
from learn import views
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

# API url routting
router = routers.DefaultRouter()
router.register(r'branch',views.BranchViewSet)
router.register(r'notice',views.NoticeViewSet)

urlpatterns = [
     path('home/', views.HomeView.as_view()),
     path('about/', views.AboutView.as_view()),
     path('contact/', views.ContactView.as_view()),
     path('', RedirectView.as_view(url="home/")),
     
#API URL Here
     path(r'api/', include(router.urls)),
     path(r'api-token-auth/', obtain_jwt_token),
     
]
