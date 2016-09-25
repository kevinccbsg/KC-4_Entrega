from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
__author__ = 'kevinccbsg'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name',
                  'username', 'password', 'email',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise ValidationError(
                "El nombre de esta usuario {0} ya está siendo utilizado".format(username))
        return username

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise ValidationError(
                "Este email {0} ya está siendo utilizado".format(email))
        return email
