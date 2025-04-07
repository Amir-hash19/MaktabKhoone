from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from books.models import CategoryArticle, Article, CategoryBook, Book
import json



def home_page(request):
    return HttpResponse("This is django project")





@csrf_exempt
def create_category_article(request):
    if request.method == "POST":
        data = json.loads(request.body)
        created_category_article = CategoryArticle.objects.create(
           name = data.get("name"),
           slug = data.get("slug") 
        )
        return HttpResponse(f"{created_category_article.id} Category was created Successfully")
    
        


@csrf_exempt
def create_category_book(request):
    if request.method == "POST":
        data = json.loads(request.body)
        created_category_book = CategoryBook.objects.create(
            name = data.get("name"),
            slug = data.get("slug")
        )
        return HttpResponse(f"{created_category_book.id} Category was created Successfully")