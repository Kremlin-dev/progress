from django.contrib import admin
from .models import Note

class NotePanel(admin.ModelAdmin):
    list_display = ("title", "content", "created_at","updated_at", "owner" )

class adminsite(admin.AdminSite):
    site_header = "NOTES"
    site_title = "Admin Notes"
    index_title ="admin"


siteadmin = adminsite(name ="siteadmin")

siteadmin.register(Note, NotePanel)
# Register your models here.
