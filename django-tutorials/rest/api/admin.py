from django.contrib import admin

from .models import userinfo

class userinfoPanel(admin.ModelAdmin):
    list_display = ("username", "email", "age")

class adminsite(admin.AdminSite):
    site_header = "DJANGO REST FRAMEWORK"
    site_title = "Admin Panel"
    index_site ="admin"

siteadmin = adminsite(name = 'siteadmin')

siteadmin.register(userinfo, userinfoPanel)



# Register your models here.
