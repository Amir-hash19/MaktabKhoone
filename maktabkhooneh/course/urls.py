from django.urls import path
from .views import user_profile, update_course, course_retrive_view, retrive_update_destroy_view, list_create_view, courselistview, create_course_view, delete_course_view, update_course_view

urlpatterns = [
    path('profile/', user_profile),
    path("update-course/<int:course_id>/", update_course),
    path('list', courselistview.as_view()),
    path('retrive/<int:pk>', course_retrive_view.as_view()),
    path('retrive_update_delete/<int:pk>', retrive_update_destroy_view.as_view()),
    path('list_create/', list_create_view.as_view()),
    path('create', create_course_view.as_view()),
    path('delete/<int:pk>', delete_course_view.as_view()),
    path('update/<int:pk>',update_course_view.as_view()),
    path('list-create', list_create_view.as_view()),
]