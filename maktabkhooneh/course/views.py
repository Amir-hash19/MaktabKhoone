from django.shortcuts import render
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Course
import json
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView,DestroyAPIView, UpdateAPIView
from course.serializer import Courseserializer, courseslistserializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
            course.name = data.get("title", course.title)
            course.description = data.get("description", course.description)
            course.price = data.get("price", course.price)
            course.save()

            return JsonResponse({"message": "Course updated successfully!"})
        except Exception:
            return JsonResponse({"error"})

    return JsonResponse({"error": "Invalid request method"})


class CourseListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = courseslistserializer


class CourseRetriveView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = Courseserializer


class RetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Course.objects.all()
    serializer_class = Courseserializer


class ListCreateView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = Courseserializer
    permission_classes = [IsAdminUser]

class CreateCourseView(CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Course.objects.all()
    serializer_class = Courseserializer

    def perform_create(self, serializer):
        serializer.save(
            creator= self.request.user
        )

class DeleteCourseView(DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Course.objects.all()
    serializer_class = CourseListView

class UpdateCourseView(UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = Courseserializer

class ActiveCoursesListView(ListAPIView):
    queryset = Course.objects.filter(is_active=True)
    serializer_class = Courseserializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class MyCoursesView(ListAPIView):
    serializer_class = Courseserializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Course.objects.filter(creator=self.request.user)
    
class UnenrollFromCourseView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, course_id):
        try:
            course = Course.objects.get(id=course_id)
            course.students.remove(request.user.student)
            return Response({"message": "Unenrolled successfully!"})
        except Course.DoesNotExist:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
        
class CourseStudentsListView(RetrieveAPIView):
    serializer_class = Courseserializer
    permission_classes = [IsAdminUser]

    def retrieve(self, request, *args, **kwargs):
        course = Course.objects.get(pk=kwargs['pk'])
        students = course.students.all()
        student_data = [{"id": s.id, "name": s.name} for s in students]
        return Response({"students": student_data})