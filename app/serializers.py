from .models import Enlace
from django.contrib.auth.models import User
from rest_framework import serializers

class EnlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Enlace
        fields = ('url', 'titulo','enlace','votos','usuario')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username','email')
