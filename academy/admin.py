from django.contrib import admin
from .models import course,trainer,Students

class academic_studies(admin.ModelAdmin):
    
    list_display = ['course_name']

# Register your models here.
admin.site.register(course,academic_studies)
admin.site.register(trainer)
admin.site.register(Students)
