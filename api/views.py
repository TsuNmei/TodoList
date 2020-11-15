from rest_framework import generics, views, permissions
from django.contrib.auth.models import User
from api.models import UserProfile, Item, Category
from api.seriliazer import *
from api import exceptions


class UserListView(generics.ListCreateAPIView):
    serializer_class = UserSeriailizer
    permissions_class = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.all().order_by('-date_joined')


class ItemListView(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    permissions_classes = [permissions.IsAuthenticated, ]
    queryset = Item.objects.all()

    # def get_queryset(self, request=None):
    #     return self.queryset.filter(user=self.request.user)


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView)
    serializer_class = ItemSerializer
    permissions_classes = [permissions.IsAuthenticated, ]
    queryset = Item.objects.all()

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)

    def perform_create(self, serializer):
        serializer.save(creatorer=self.request.user)


class CategoryListView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permissions_classes = [permissions.IsAuthenticated, ]
    queryset = Category.objects.all()

    # def get_queryset(self, request=None):
    #     return self.queryset.filter(user=self.request.user)


class CategoryDetailView(generics.UpdateDestroyAPIView):
    serializer_class = CategorySerializer
    permissions_classes = [permissions.IsAuthenticated, ]
    queryset = Category.objects.all()

    # def get_queryset(self):
    #     return self.queryset.filter(creator=self.request.user)

    # def perform_create(self, serializer):
    #     serializer.save(creatorer=self.request.user)
