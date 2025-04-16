from django.urls import path
from .views import (
    CreateUserView, DeleteUserView
    )
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView,
    )

urlpatterns = [
    path("create-account", CreateUserView.as_view()),
    path("delete-account", DeleteUserView.as_view()),
    path("obtain-token", TokenObtainPairView.as_view()),
    path("refresh-token", TokenRefreshView.as_view()),
    path("verify-token", TokenVerifyView.as_view())
]
