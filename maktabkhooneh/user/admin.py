from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("user_name", "first_name", "email")
    list_filter = ("birth_date", )
    search_fields = ("user_name", "birth_date")
    list_per_page = 30





    def get_ordering(self, request):
                        if request.user.is_superuser:
                                return ("name", "-date_created")
                        return ("is_active", )
                
                        
                
            
                
            