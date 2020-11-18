from rest_framework import serializers
from api.models import UserProfile, Category, Item, ItemImage
from django.contrib.auth.admin import User


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    account = serializers.CharField()
    password = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = serializers.ALL_FIELDS


class LoginSerializer(serializers.Serializer):
    account = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = serializers.ALL_FIELDS


class CatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = serializers.ALL_FIELDS


class CatDetailserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'color']


class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = serializers.ALL_FIELDS


class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['title', 'description', 'priority']


class BatchDeleteForm(serializers.Serializer):
    items = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all(), many=True)

    class Meta:
        model = Item


class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = serializers.ALL_FIELDS
