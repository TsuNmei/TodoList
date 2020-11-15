from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # APIView
    path('token-auth/', obtain_auth_token, name='api_token_auth'),
    path('item/', views.ItemListView.as_view(), name='get_items'),
    path('item/<int:user_id>', views.ItemDetailView.as_view(), name='update_items'),

]