from django.contrib.auth.models import User, Group
from rest_framework.serializers import HyperlinkedModelSerializer as HMS
from rightmove.api.models import Content

class UserSerializer(HMS):
    class Meta:
        model = User
        fields = ('url','username','email','groups')

class GroupSerializer(HMS):
    class Meta:
        model = Group
        fields = ('url','name')

class ContentSerializer(HMS):
    class Meta:
        model = Content
        fields = ('instance_name','content_body','css_tag')
