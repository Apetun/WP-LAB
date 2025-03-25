from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Default landing page for /directory/
    path('insert_works/', views.insert_works, name='insert_works'),
    path('query_company/', views.query_company, name='query_company'),
]
