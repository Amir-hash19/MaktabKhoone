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
    



@csrf_exempt
def delete_category_arthicle(request, cat_id):
    if request.method == "DELETE":
        category = get_object_or_404(CategoryArticle, id=cat_id)
        category.delete()
        return HttpResponse("The category was deleted Successfully")





@csrf_exempt
def delete_category_book(request, cat_id):
    try:
        cat_id = CategoryBook.objects.get(id=cat_id)
    except CategoryBook.DoesNotExist:
        return HttpResponse("The Category Does not exist!")
    cat_id.delete()
    return HttpResponse("The category was Deleted Successfully")    






@csrf_exempt
def display_category_book(request, cat_id):
    try:
        category = CategoryBook.objects.get(id=cat_id)
        category_data = {
            "id":category.id,
            "name":category.name,
            "slug":category.slug
        }
        return JsonResponse(category_data, safe=True)
    except CategoryBook.DoesNotExist:
        return JsonResponse({"error":"Category not found!"})




@csrf_exempt
def display_category_article(request, cat_id):
    try:
        category = CategoryArticle.objects.get(id=cat_id)
        category_data = {
            "id":category.id,
            "name":category.name,
            "slug":category.slug
        }
        return JsonResponse(category_data, safe=True)
    except CategoryBook.DoesNotExist:
        return JsonResponse({"error":"Category not found!"})





