from django.urls import path
from .views import home_page,create_category_article, create_category_book

urlpatterns = [
    path("", home_page, name="home-page"),
    path("create-category-article/", create_category_article, name="create-category-article"),
    path("create-category-book/", create_category_book, name="create-category-book"),
]
