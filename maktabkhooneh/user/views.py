from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import User
from datetime import date, datetime
from django.contrib.auth.hashers import make_password,check_password


def home_page(request):
    return HttpResponse("Welcome and This is landing page!")



@csrf_exempt
def create_account(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        birth_date_str = data.get("birthDate")  # e.g., '2006-04-06'
        if birth_date_str:
            birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
            if calculate_age(birth_date) >= 18:
                user = User.objects.create(
                    user_name = data.get("userName"),
                    password = make_password(data.get("password")),
                    phone_number = data.get("phoneNumber"),
                    birth_date = birth_date
                )
                return JsonResponse({
                    "user_id":user.id,
                    "user_name":user.user_name
                    })
            else:
                return HttpResponse("user is under 18")
        else:
            return HttpResponse("ERROR")



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



def calculate_age(birth_date):
    if birth_date is None:
        return None
    today = date.today()
    return int(today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day)))



@csrf_exempt
def update_user_info(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            user = User.objects.get(id = data.get("userId"))
        except:
            return HttpResponse("user does not exist")
        
        if check_password(data.get("oldPassword"), user.password):
            user.user_name = data.get("userName")
            user.first_name = data.get("userName")
            user.last_name = data.get("userName")
            user.password = make_password(data.get("password"))
            user.birth_date = data.get("birthDate")
            user.phone_number = data.get("phoneNumber")
            user.email = data.get("email")
            return HttpResponse("user updated")
        else:
            return HttpResponse("wrong password")


@csrf_exempt
def see_user_info(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            user = User.objects.get(id = data.get("userId"))
            entered_password = data.get("password")
            if check_password(entered_password, user.password):
                user_data = User.objects.filter(id=user.id).values().first()
                return JsonResponse(user_data)
            else:
                return HttpResponse("Wrong password")
        except:
            return HttpResponse("user does not exist")
