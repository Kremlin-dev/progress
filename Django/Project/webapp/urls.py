from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.authenticate, name='authenticate')
]