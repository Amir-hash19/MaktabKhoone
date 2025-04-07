from django.contrib import admin
from django.utils import timezone
from .models import (Article, CategoryArticle
                     ,CategoryBook,Book)



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title","date_create","slug")
    list_filter = ("title", "date_create", "update_at", "author")
    prepopulated_fields = {'slug': ('title',)}      
    search_fields = ("title", "author", "slug")
    ordering = ["-date_create"]
    list_per_page = 20


    

@admin.register(CategoryArticle)
class CategoryArticleAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {'slug': ('name',)} 
    search_fields = ("name", )
    list_per_page = 30



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "date_created","status")
    list_filter = ("date_created", "status", "category")
    search_fields = ("status", "category", "title")
    fields = (("title", "slug"), "description", "status")
    list_per_page = 30


    def get_ordring(self, request):
        if request.user.is_superuser:
            return ("title", "-date_created")
        return ("title", )
    
    
    def day_since_creation(self, book):
        diff = timezone.now() - book.date_created()
        return diff.days
    day_since_creation.short_description = "Days Active"



    def set_book_to_published(self, request, queryset):
        count = queryset.update(status="published")
        self.message_user(request, "{}.The selected book have been published".format(count))

    set_book_to_published.short_description = "mark selected book as published"    

    
    
    
@admin.register(CategoryBook)
class CategoryBookAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", )
         
