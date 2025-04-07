from django.urls import path
from .views import (home_page,create_category_article, create_category_book,
                               delete_category_arthicle,delete_category_book, display_category_book, display_category_article)

urlpatterns = [
    path("", home_page, name="home-page"),
    path("create-category-article/", create_category_article, name="create-category-article"),
    path("create-category-book/", create_category_book, name="create-category-book"),
    path("delete-category-arthicle/<int:cat_id>", delete_category_arthicle, name="delete-category-arthicle"),
    path("delete-category-book/<int:cat_id>", delete_category_book, name="delete-category-book"),
    path("display-category-book/<int:cat_id>", display_category_book, name="display-category-book"),
    path("display-category-article/<int:cat_id>", display_category_article, name="display-category-article"),
    

]
