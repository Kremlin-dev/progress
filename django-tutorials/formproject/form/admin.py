from django.contrib import admin
from .models import register

class registeradmin(admin.ModelAdmin):
    list_display = ("firstName", "lastName", "email", "telephone")

admin.site.register(register, registeradmin)

# Register your models here.
