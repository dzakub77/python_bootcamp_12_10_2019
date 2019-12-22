from django.contrib import admin

# Register your models here.
from cars.models import Engine, Car

admin.site.register(Car)
admin.site.register(Engine)