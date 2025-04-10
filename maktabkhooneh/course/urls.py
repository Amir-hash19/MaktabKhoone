from django.urls import path
from .views import user_profile, update_course, courselist

urlpatterns = [
    path('profile/', user_profile),
    path("update-course/<int:course_id>/", update_course),
    path('course-list', courselist.as_view()),
]