from django.contrib import admin
from .models import todolist
from django.contrib.auth.models import User
class todolistpanel(admin.ModelAdmin):
    list_display = ("title", "description", "completed","category", "priority")

class siteadmin(admin.AdminSite):
    site_header="adminsite"
    site_title ="TodoList"
    index_title="todo"

class UserPanel(admin.ModelAdmin):
    list_display = ("username", "password")
adminsite = siteadmin(name = 'siteadmin')


adminsite.register(todolist, todolistpanel)
adminsite.register(User, UserPanel)
# Register your models here.
