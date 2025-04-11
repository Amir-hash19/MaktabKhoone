from django.shortcuts import render
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Course
import json
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView,DestroyAPIView
from course.serializer import Courseserializer, courseslistserializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

@login_required
def user_profile(request):
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
        return JsonResponse({"error": "Course not found"})

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


class courselistview(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = courseslistserializer


class course_retrive_view(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = Courseserializer


class retrive_update_destroy_view(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Course.objects.all()
    serializer_class = Courseserializer


class list_create_view(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = Courseserializer
    permission_classes = [IsAdminUser]

class create_course_view(CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Course.objects.all()
    serializer_class = Courseserializer

    def perform_create(self, serializer):
        serializer.save(
            creator= self.request.user
        )

class delete_course_view(DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Course.objects.all()
    serializer_class = courselistview
