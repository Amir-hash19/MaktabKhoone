from django.shortcuts import render
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Course
import json

@login_required
def  user_profile(request):
    user_data= {
        'name':request.user.name, 
        'email_address':request.user.email, 
        'phone_number' :request.user.email,
    }
    return JsonResponse (user_data)

@csrf_exempt
def update_course(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return JsonResponse({"error": "Course not found"}, status=404)

    if request.method == "POST" or request.method == "PUT":
        try:
            data = json.loads(request.body)
            course.title = data.get("title", course.title)
            course.description = data.get("description", course.description)
            course.price = data.get("price", course.price)
            course.save()

            return JsonResponse({"message": "Course updated successfully!"})
        except Exception:
            return JsonResponse({"error"})

    return JsonResponse({"error": "Invalid request method"})
