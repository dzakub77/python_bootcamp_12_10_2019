from django.contrib import admin
from maths.models import Math, Category

# Register your models here.

class AdminMath(admin.ModelAdmin):
    list_display = ["id", 'operation', 'a', 'b', 'resault']
    list_filter = ['operation']
    search_fields = ['resault']

admin.site.register(Math, AdminMath)
admin.site.register(Category)