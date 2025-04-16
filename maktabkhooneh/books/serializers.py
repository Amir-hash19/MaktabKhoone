from rest_framework import serializers
from .models import Article, Book



class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"



class ArticleSerializerDate(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["date_create"]



class BookSerializerDate(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"





class SendOTPSerializer(serializers.Serializer):
    phone = serializers.CharField()




class VerifyOTPSerializer(serializers.Serializer):
    phone = serializers.CharField()
    code = serializers.CharField()
    