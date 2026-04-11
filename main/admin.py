from django.contrib import admin
from .models import Cars
from .models import Models

admin.site.register(Models)
admin.site.register(Cars)

# Register your models here.
