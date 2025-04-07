from django.contrib import admin
from django.urls import path,include



admin.site.site_header = "MaktabKhoone"
admin.site.site_title = "MaktabKhoone"
admin.site.index_title = "MaktabKhonne"




urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("user.urls")),
    path("course/", include("course.urls")),
    path("arthicle/", include("books.urls")),
]


