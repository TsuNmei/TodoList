from rest_framework import generics, views, permissions, response, status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from api.models import UserProfile, Item, Category
from api.serializers import *
from api import exceptions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


# class ProfileListView(views.APIView):
#     serializer_class = ProfileSerializer
#     permissions_class = [permissions.IsAuthenticated]
#
#     def get(self, request):
#         print(self.request.user)
#         profile = self.request.user.profile
#         serializers = self.serializer_class(profile, many=True)
#         return response.Response(serializers.data, 200)


class ItemListView(generics.ListCreateAPIView):
    serializer_class = ItemListSerializer
    permissions_classes = [permissions.IsAuthenticated]
    queryset = Item.objects.all()

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user.profile)

    def create(self, request, *args, **kwargs):
        serializers = self.serializer_class(data=request.data)
        serializers.is_valid(raise_exception=True)
        val_data = serializers.validated_data
        creator = val_data.get('creator')

        if creator != self.request.user.profile:
            raise exceptions.InvalidUser()
        instance = serializers.save(creator=self.request.user.profile)
        return response.Response(self.serializer_class(instance).data, 201)


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemDetailSerializer
    permissions_classes = [permissions.IsAuthenticated]
    queryset = Item.objects.all()
    lookup_field = 'id'

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user.profile)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user.profile)

    def update(self, request, *args, **kwargs):
        return response.Response({'update success'}, 200)


class CategoryListView(generics.ListCreateAPIView):
    serializer_class = CatListSerializer
    permissions_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()

    def get_queryset(self, request=None):
        return self.queryset.filter(creator=self.request.user.profile)

    def create(self, request, *args, **kwargs):
        serializers = self.serializer_class(data=request.data)
        serializers.is_valid(raise_exception=True)
        val_data = serializers.validated_data
        creator = val_data.get('creator')

        if creator != self.request.user.profile:
            raise exceptions.InvalidUser()
        instance = serializers.save(creator=self.request.user.profile)
        return response.Response(self.serializer_class(instance).data, 201)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CatDetailserializer
    permissions_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
    lookup_field = 'id'

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user.profile)


class UserRegister(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return response.Response({'error': 'not valid'})
        val_data = serializer.validated_data
        try:
            user = User.objects.create_user(username=val_data['account'], password=val_data['password'])
            profile = UserProfile.objects.create(user=user, name=val_data['username'])
        except:
            raise exceptions.UserExist()

        return response.Response({'created success'}, 201)


class UserLogin(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        # data = {
        #     'username':request.data.get('account'),
        #     'password':request.data.get('password')
        # }
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            creator = user.profile
        except:
            raise exceptions.CantNotFound()

        token, created = Token.objects.get_or_create(user=user)
        return response.Response({'userid': creator.id, 'username': creator.name, 'token': token.key})
