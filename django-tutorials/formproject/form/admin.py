from django.contrib import admin

from .models import hostel


class hostelpanel(admin.ModelAdmin):
    list_display =("hostelName", "location", "manager", "phone", "rooms")


class adminsite(admin.AdminSite):
    site_header = "Campus Hostel Finder Panel"
    site_title = "Manager Panel"
    index_site = "CHF admin"

siteadmin = adminsite(name='siteadmin')

siteadmin.register(hostel, hostelpanel)