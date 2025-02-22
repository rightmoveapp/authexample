"""rightmove URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework.routers import DefaultRouter

from rightmove.api import views

router = DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'group', views.GroupViewSet)
router.register(r'content',views.ContentViewSet)

urlpatterns = [

    path('', include(router.urls)),
    re_path(r'^rest-auth/github/$', views.GithubLogin.as_view(), name='github_login'),
    re_path(r'^rest-auth/facebook/$', views.FacebookLogin.as_view(), name='fb_login'),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
