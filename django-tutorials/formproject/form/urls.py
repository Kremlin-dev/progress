from django.urls import path


urlpatterns =[
    path('', views.home, name='home'),
    path('register/', views.signup, name='signup')
]