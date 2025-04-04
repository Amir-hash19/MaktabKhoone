from django.urls import path
from .views import create_account, delete_account

urlpatterns = [
    path("create-account", create_account),
    path("delete-account", delete_account)
]