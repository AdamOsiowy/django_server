from ..shared_functions import *
from django.shortcuts import render

GITHUB_API_URL = 'https://api.github.com'


def home_view(request):
    return render(request, "repos_viewer/home.html")
