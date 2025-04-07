from django.urls import path
from .views import create_account, delete_account, see_user_info, update_user_info, home_page

urlpatterns = [
    path("", home_page),
    path("create-account", create_account),
    path("delete-account", delete_account),
    path("user_info", see_user_info),
    path("update-info", update_user_info)
]