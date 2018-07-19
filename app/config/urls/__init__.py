from django.contrib import admin
from django.urls import path, include
from . import django_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('snippets/', include(django_view))
]
