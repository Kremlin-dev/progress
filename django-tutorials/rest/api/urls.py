from django.urls import path

from . import views
from .views import dataView

urlpatterns = [
    path('', views.getdata, name = 'getdata'),
    path('postdata/', views.postdata, name ='postdata'),
    path('serial/', dataView.as_view(), name = 'dataView'),
]