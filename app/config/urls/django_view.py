from django.urls import path
from snippets.views import django_view

app_name = 'snippets'

urlpatterns = [
    path('django_view/snippets/', django_view.snippet_list, name='snippet-list'),
    path('django_view/snippets/<int:pk>/', django_view.snippet_detail, name='snippet-detail')
]