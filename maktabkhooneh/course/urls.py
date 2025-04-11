from django.urls import path
from .views import user_profile, update_course, course_retrive_view, retrive_update_destroy_view, list_create_view, courselistview

urlpatterns = [
    path('profile/', user_profile),
    path("update-course/<int:course_id>/", update_course),
    path('course-list', courselistview.as_view()),
    path('course_retrive/<int:pk>', course_retrive_view.as_view()),
    path('retrive_update_delete/<int:pk>', retrive_update_destroy_view.as_view()),
    path('list_create/', list_create_view.as_view()) 
]