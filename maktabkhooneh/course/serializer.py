from rest_framework.serializers import ModelSerializer
from course.models import Course

class Courseserializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['name']