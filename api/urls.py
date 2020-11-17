from django.urls import path
from api import views
from rest_framework.authtoken.views import obtain_auth_token
# from revauth import views as view


urlpatterns = [
    path('item/', views.ItemListView.as_view(), name='get_items'),
    path('item/<int:id>', views.ItemDetailView.as_view(), name='update_items'),
    path('category/', views.CategoryListView.as_view(), name='get_categories'),
    path('category/<int:id>', views.CategoryDetailView.as_view(), name='update_categories'),

    path('user/register', views.UserRegister.as_view(), name='create-userprofile'),
    path('user/login', views.UserLogin.as_view(), name='auth-login'),
    # path('user/login', obtain_auth_token, name='api_token_auth'),
    # path('user/profile', views.ProfileListView.as_view(), name='get_profile'),
    # path('user/register', views.UserCreate.as_view(), name='api_create_user'),
    # path('user/refresh', view.RefreshProfile.as_view(), name='auth-refresh'),
]
