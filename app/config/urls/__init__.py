from django.contrib import admin
from django.urls import path, include
from . import django_view
from . import mixins, generic_cbv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('snippets/', include(django_view)),
    path('mixin/', include(mixins)),
    path('generic/', include(generic_cbv)),
]
