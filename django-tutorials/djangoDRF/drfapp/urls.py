from django.urls import path
from . import views

urlpatterns =[
    path("", views.create_note, name="created_note"),
    path("getnote/", views.get_note, name = "get_note"),
    path("updatenote/<int:id>/", views.update_note, name="update_note"),
    path("deletenote/<int:id>/", views.delete_note, name="delete_note")
]