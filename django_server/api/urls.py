from .views import *
from django.urls import path, re_path

urlpatterns = [
    path('<str:name>', get_user_view, name='get_user'),
    path('<str:name>/', get_user_view, name='get_user/'),
    path('<str:name>/<str:repo_name>', get_repo_view, name='get_repo'),
    path('<str:name>/<str:repo_name>/', get_repo_view, name='get_repo/'),
]
