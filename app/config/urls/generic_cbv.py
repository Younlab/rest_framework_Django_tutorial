from django.urls import path
from snippets.views import generic_cbv as views
urlpatterns = [
    path('snippets/users/', views.UserList.as_view(),name='snippet-list'),
    path('snippets/users/<int:pk>/', views.UserDetail.as_view(),name='snippet-detail'),
]