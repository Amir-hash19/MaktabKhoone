from django.urls import path
from .views import (
    user_profile,
    update_course,
    CourseRetriveView,
    RetrieveUpdateDestroyView,
    CourseListView,
    CreateCourseView,
    DeleteCourseView,
    UpdateCourseView,
    ListCreateView,
    ActiveCoursesListView,
    MyCoursesView,
    UnenrollFromCourseView,
    CourseStudentsListView,
)


urlpatterns = [
    path('profile/', user_profile),
    path("update-course/<int:course_id>/", update_course),
    path('list/', CourseListView.as_view()),
    path('retrive/<int:pk>', CourseRetriveView.as_view()),
    path('retrive_update_delete/<int:pk>', RetrieveUpdateDestroyView.as_view()),
    path('list_create/', ListCreateView.as_view()),
    path('create/', CreateCourseView.as_view()),
    path('delete/<int:pk>', DeleteCourseView.as_view()),
    path('update/<int:pk>',UpdateCourseView.as_view()),
    path('listcreate/', ListCreateView.as_view()),
    path('courses/active/', ActiveCoursesListView.as_view()),
    path('courses/mine/', MyCoursesView.as_view()),
    path('courses/<int:course_id>/unenroll/', UnenrollFromCourseView.as_view()),
    path('courses/<int:course_id>/students/', CourseStudentsListView.as_view()),
]