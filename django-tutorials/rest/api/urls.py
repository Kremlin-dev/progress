from django.urls import path

from . import views

urlpatterns = [
    path('', views.getdata, name = 'getdata'),
    path('postdata/', views.postdata, name ='postdata')
]