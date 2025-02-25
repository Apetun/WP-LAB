from django.contrib import admin
from django.urls import path, include
from formapp.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('formapp.urls')),
    path('', home_view, name='home'),
]
