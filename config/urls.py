from django.contrib import admin
from django.urls import path

from core.views import index, contact

urlpatterns = [
    path('admin/', admin.site.urls),  # админка
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
]
