from . import views
from django.urls import path, re_path

urlpatterns = [
    path('<str:name>', views.get_user_view, name='get_user'),
    path('<str:name>/', views.get_user_view, name='get_user/'),
]
