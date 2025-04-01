from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/new/', views.create_book, name='create_book'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
]

