from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='homepage'),
    path('bookslist/', views.book_list, name='booklist'),
    path('bookdetails/<int:id>', views.book_detail, name='bookdetail'),
    path('addbook/', views.add_book, name='addbook'),
    path('updatebook/', views.update_book, name='updatebook'),
    path('deletebook/', views.delete_book, name='deletebook'),
]