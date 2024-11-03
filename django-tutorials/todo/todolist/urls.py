from django.urls import path
from . import views

urlpatterns =[

    path('register/', views.sign_up, name = "signup"),
    path('login/', views.login, name = "login"),
    path('posttodo/', views.postodo, name = "todo"),
    path('getalltodo/', views.getalltodo, name= 'getalltodo'),
    path('gettodo/<int:id>/', views.gettodo, name = 'gettodo'),
    path('updatetodo/<int:id>/', views.puttodo, name = 'puttodo'),
    path('deletetodo/<int:id>/', views.deletetodo, name='deletetodo') 
]