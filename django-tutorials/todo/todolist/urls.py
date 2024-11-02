from django.urls import path
from . import views

urlpatterns =[
    path('posttodo/', views.postodo, name = "todo"),
    path('getalltodo', views.getalltodo, name= 'getalltodo'),
    path('gettodo', views.gettodo, name = 'gettodo'),
    path('updatetodo', views.puttodo, name = 'puttodo'),
    path('deletetodo/', views.deletetodo, name='deletetodo')
    
]