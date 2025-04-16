from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView,CreateAPIView
from .serializers import ArticleSerializer, BookSerializerDate, SendOTPSerializer, VerifyOTPSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from books.models import CategoryArticle, Article, CategoryBook, Book, OTP
from django.http.response import HttpResponse, JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.contrib.auth.models import User 
from rest_framework.views import APIView
from rest_framework import status
from .utils.sms import SMSClient
import json






#OTP Authentication!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
User = get_user_model()
class SendOTPView(APIView):
    def post(self, request):
        serializer = SendOTPSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data["phone"]
            code = OTP.generate_code()
            OTP.objects.create(phone=phone, code=code)
            SMSClient().send_otp(phone, code)
            return Response({"details":"code has been sent!"})
        return Response(serializer.errors, status=400)


class VerifyOTPView(APIView):
    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data["phone"]
            code = serializer.validated_data["code"]
            otp = OTP.objects.filter(phone=phone, code=code).last()
            if otp and otp.is_valid():
                user, created = User.objects.get_or_create(username=phone)
                token = RefreshToken.for_user(user)
                return Response({
                    "refresh":str(token),
                    "access":str(token.access_token)
                })
            return Response({"details":"the code is expired or invalidated!"}, status=400)
        return Response(serializer.errors, status=400)






#RESTframeworkAPI!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializerDate
   

class ListBookView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializerDate



class ArticleListCreateView(ListCreateAPIView):
     queryset = Article.objects.all()
     serializer_class = ArticleSerializer


class ArticleRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer



def home_page(request):
    return HttpResponse("This is django project")



class ArticleListView(ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()



class ArticleTimeListView(ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.order_by("-date_create")


class ArticleRetrieView(RetrieveAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()



        







#Function base views!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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






@csrf_exempt
def create_book(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            category_id = data.get("category_id")
            author_id = data.get("author_id")
            if not category_id and not author_id:
                return JsonResponse({"error":"category_id and author_id is required"}, status=400)
            
            try:
                category = CategoryBook.objects.get(id=category_id)
            except CategoryBook.DoesNotExist:
                return JsonResponse({"error":"category does not exist!"}, status=404)
            
            try:
                author = User.objects.get(id=author_id)
            except User.DoesNotExist:
                return JsonResponse({"error":"author does not exist"}, status=404)    

            
            created_book = Book.objects.create(
                title=data.get("title"),
                description=data.get("description"),
                slug=data.get("slug"),
                status=data.get("status"),
                quantity=data.get("quantity"),
                author=author,
                category=category
            )
            return JsonResponse({"message":f"Book with ID {created_book.id} created Succesfully"})

        except json.JSONDecodeError:
            return JsonResponse({"error":"Invalid Json data"})
        
    return JsonResponse({"error":"Invalid request method"}, status=405)        






@csrf_exempt
def create_arthicle(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            category_id = data.get("category_id")
            author_id = data.get("author_id")

            if not category_id and not author_id:
                return JsonResponse({"error":"category_id and author_id is required!"}, status=400)
            
            try:
                category = CategoryArticle.objects.get(id=category_id)
            except CategoryArticle.DoesNotExist:
                return HttpResponse("The category does not exist!")
            
            try:
                author = User.objects.get(id=author_id)
            except User.DoesNotExist:
                return HttpResponse("The User does not exist!")
                

            created_arthicle = Article.objects.create(
                title = data.get("title"),
                description = data.get("description"),
                slug = data.get("slug"),
                category = category,
                author = author
            )
            return JsonResponse({"message":f" Article with ID {created_arthicle.id} created Succesfully"})
        except json.JSONDecodeError:
            return JsonResponse({"error":"Invalid Json data"}, status=405)
        
    return JsonResponse({"ERROR":"Invalid request method"}, status=405)




@csrf_exempt
def update_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return JsonResponse({"ERROR":"book not found!"}, status=404) 


    try:
        if request.method in ["PUT","PATCH"]:
            try:
                data = json.loads(request.body)
            except json.JSONDecodeError:
                return JsonResponse({"error":"Invalid Json format"}, status=400)

            try:
                if request.method == "PUT":
                    book.title = data.get("book", book.title)
                    book.description = data.get("description", book.description)
                    book.slug = data.get("slug", book.slug)
                    book.status = data.get("status", book.status)
                    book.quantity = int(data.get("quantity", book.quantity))
                    if "author" in data:
                        book.author = User.objects.get(id=int(data["author"]))
                    if "category" in data:
                        book.category = User.objects.get(id=int(data["category"]))    
                elif request.method == "PATCH":
                    if "title" in data:
                        book.title = data["title"]
                    if "description" in data:
                        book.description = data["description"]
                    if "slug" in data:
                        book.slug = data["slug"]
                    if "quantity" in data:
                        book.quantity = data["quantity"]
                    if "status" in data:
                        book.status = data["status"]
                    if "category" in data:
                        book.category = CategoryBook.objects.get(id=int(data["category"]))   
                    if "author" in data:
                        book.author = User.objects.get(id=int(data["author"]))

                book.save()
                return JsonResponse({"message":"The book updated Successfully!"}, status=200)
            except ValueError:
                return JsonResponse({"ERROR":"Invalid data type"})
    except json.JSONDecodeError:
        return HttpResponse("invalid data inserted!")        
    return JsonResponse({"ERROR":"Invalid request method"}, status=405)            
    

   
        
        



