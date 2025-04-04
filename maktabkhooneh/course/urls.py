from django.urls import path
from .views import user_profile, update_course

urlpatterns = [
    path('profile/', user_profile),
    path("update-course/<int:course_id>/", update_course),
]