from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.urls import path
from .views import (home_page,create_category_article, create_category_book,
                               delete_category_arthicle,delete_category_book, 
                               display_category_book, display_category_article,
                                 create_book, create_arthicle, update_book, ArticleListView, ArticleTimeListView, ArticleRetrieView,
                                 ArticleRetrieveUpdateDestroyView ,ArticleListCreateView, BookCreateView, SendOTPView, VerifyOTPView)

urlpatterns = [
    path("", home_page, name="home-page"),
    path("create-category-article/", create_category_article, name="create-category-article"),
    path("create-category-book/", create_category_book, name="create-category-book"),
    path("delete-category-arthicle/<int:cat_id>", delete_category_arthicle, name="delete-category-arthicle"),
    path("delete-category-book/<int:cat_id>", delete_category_book, name="delete-category-book"),
    path("display-category-book/<int:cat_id>", display_category_book, name="display-category-book"),
    path("display-category-article/<int:cat_id>", display_category_article, name="display-category-article"),
    path("create-book/", create_book, name="create-book"),
    path("create-arthicle", create_arthicle, name="create-arthicle"),
    path("update_book/<int:book_id>", update_book, name="update-book"),
    ##################################################################################
    path("list-article", ArticleListView.as_view(), name="listarticle"),
    path("filter-by-time",ArticleTimeListView.as_view()),
    path("article-retrie/<int:pk>", ArticleRetrieView.as_view()),
    path("create-list/", ArticleListCreateView.as_view()),
    path("update-delete-retriev/<int:pk>", ArticleRetrieveUpdateDestroyView.as_view()),
    path("create-book", BookCreateView.as_view()),
    path("send-otp/", SendOTPView.as_view()),
    path("verify-otp", VerifyOTPView.as_view()),
]
