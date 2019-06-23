from django.contrib.auth.models import User, Group 
from rightmove.api.models import Content
from rest_framework.viewsets import ModelViewSet as MVS
from rightmove.api.serializers import UserSerializer, GroupSerializer,ContentSerializer
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView

class UserViewSet(MVS):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(MVS):
    queryset= Group.objects.all()
    serialzier_class= GroupSerializer

class ContentViewSet(MVS):
    queryset= Content.objects.all()
    serializer_class= ContentSerializer

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

class GithubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = "http://localhost:8000"
    client_class = OAuth2Client

