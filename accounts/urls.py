from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, CurrentUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', obtain_auth_token, name='api_token_auth'), 
    path('me/', CurrentUserView.as_view(), name='current_user'),
]