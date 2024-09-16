from django.contrib import admin
from .models import register

class myadminsite(admin.AdminSite):
    site_header = "REGISTER ADMIN"
    site_title = 'Kremlin-Dev'
    index_title = "admin"

siteadmin = myadminsite(name='kremlin')

class registeradmin(admin.ModelAdmin):
    list_display = ("firstName", "lastName", "email", "telephone")

siteadmin.register(register, registeradmin)

# Register your models here.
