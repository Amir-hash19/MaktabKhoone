from django.contrib import admin
from course.models import Course, Teacher, Student, Category
from django.utils import timezone




@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "email_address", "date_created")
    search_fields = ("name", "email_address")
    list_filter = ("name", "date_created")
    ordering = ("-date_created", )
    readonly_fields = ('date_created', )
    list_per_page = 30


    def get_ordering(self, request):
        if request.user.is_superuser:
            return ("name", "-date_created")
        return ("name", )
    

    

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "date_created")
    search_fields = ("name",)
    list_filter = ("name", "date_created")
    ordering = ("date_created",)   
    list_per_page = 30

    def get_ordering(self, request):
        if request.user.is_superuser:
            return ("name", "date_created")
        return ("email_address", )
    


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name", )



@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "date_created")
    list_filter = ("date_created", "price")
    search_fields = ("is_active", "name", "date_created")
    fields = (("name", "price"), "teachers", "is_active")
    list_per_page = 30

    def get_ordering(self, request):
            if request.user.is_superuser:
                return ("name", "-date_created")
            return ("is_active", )
    


    def day_since_creation(self, course):
        diff = timezone.now() - course.date_created()
        return diff.days
    day_since_creation.short_description = "days active!"
        


    def set_course_to_deactive(self, request, queryset):
        count = queryset.update(is_active=True)
        self.message_user(request, "{}the selected course has been activated ".format(count))
            

    set_course_to_deactive.short_description = "The mark selected Course is Activated"        
        





