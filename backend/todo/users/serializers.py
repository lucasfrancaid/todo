from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    def create(self, request):
        username = self.data.get('username')
        password = self.data.get('password')

        user = User(username=username)
        user.set_password(password)
        user.save()

        return self.data

    class Meta:
        model = User
        fields = ('username', 'password')
