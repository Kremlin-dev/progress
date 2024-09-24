from django.urls import path
from . import views

urlpatterns =[
    path("", views.create_note, name="created_note"),
    path("getnote/", views.get_note, name = "get_note"),
    path("updatenote/", views.update_note, name="update_note"),
    path("deletenote/", views.delete_note, name="delete_note")
]