from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/add/', views.add_category, name='add_category'),
    path('pages/add/', views.add_page, name='add_page'),
    path('categories/', views.list_categories, name='list_categories'),
    path('pages/', views.list_pages, name='list_pages'),
]
