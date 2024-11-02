from django.contrib import admin
from .models import todolist

class todolistpanel(admin.ModelAdmin):
    list_display = ("title", "description", "completed")

class siteadmin(admin.AdminSite):
    site_header="adminsite"
    site_title ="TodoList"
    index_title="todo"
adminsite = siteadmin(name = 'siteadmin')

adminsite.register(todolist, todolistpanel)
# Register your models here.
