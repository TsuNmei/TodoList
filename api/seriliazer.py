from rest_framework import serializers
from api.models import *
from django.contrib.auth.admin import User


class UserSeriailizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
