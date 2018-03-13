# Native Python Modules.

# External Modules.
from rest_framework import serializers as rest_serializers
from rest_framework.validators import UniqueValidator

# Django Modules.

# Project Modules.
from core import validators
from .models import Account


class AccountSerializer(rest_serializers.HyperlinkedModelSerializer):
    gender = rest_serializers.ChoiceField(choices=Account.GENDERS, required=True)
    firstname = rest_serializers.CharField(max_length=255, required=True)
    lastname = rest_serializers.CharField(max_length=255, required=True)
    email = rest_serializers.EmailField(required=True, validators=[UniqueValidator(Account.objects.all())])
    birthdate = rest_serializers.DateField(required=True, validators=[validators.birthday_validation])

    class Meta:
        model = Account
        fields = (
            'gender',
            'firstname',
            'lastname',
            'email',
            'birthdate',
        )
