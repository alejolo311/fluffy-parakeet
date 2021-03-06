from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import (
    UserRegistrationView,
    UserLoginView
)

urlpatterns = [
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view()),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view()),
    path('register', UserRegistrationView.as_view(), name='register'),

    path('login', UserLoginView.as_view(), name='login'),
]
