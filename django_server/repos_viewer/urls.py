from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('<str:name>', views.user_view, name='user'),
    path('<str:name>/', views.user_view, name='user/'),
    path('<str:name>/<str:repo_name>', views.repo_view, name='repo'),
    path('<str:name>/<str:repo_name>/', views.repo_view, name='repo/'),
]
