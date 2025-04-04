from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import User
# Create your views here.

@csrf_exempt
def create_account(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.create(
            user_name = data.get("userName"),
            password = data.get("password"),
            phone_number = data.get("phoneNumber")
        )
        return JsonResponse({
            "user_id":user.id,
            "user_name":user.user_name
            })
        
@csrf_exempt
def delete_account(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.get(id = data.get("userId"))
        if user.password == data.get("password"):
            user.delete()
            return JsonResponse({"status":"user deleted"})
        else:
            return JsonResponse({"status":"ERROR"})
            