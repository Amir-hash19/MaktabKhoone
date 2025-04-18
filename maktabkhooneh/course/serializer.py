from rest_framework.serializers import ModelSerializer
from course.models import Course

class Courseserializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class courseslistserializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'price']