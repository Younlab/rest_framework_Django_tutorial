from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets.views import django_view
from snippets.views import api_view as views

app_name = 'snippets'

urlpatterns = [
    path('django_view/snippets/', django_view.snippet_list, name='snippet-list'),
    path('django_view/snippets/<int:pk>/', django_view.snippet_detail, name='snippet-detail'),
    path('snippets/', views.SnippetList.as_view(),name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(),name='snippet-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)


