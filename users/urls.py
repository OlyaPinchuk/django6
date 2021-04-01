from django.urls import path
from .views import UserListCreateView, CarCreate

urlpatterns = [
    path('', UserListCreateView.as_view(), name='users_list_create'),
]