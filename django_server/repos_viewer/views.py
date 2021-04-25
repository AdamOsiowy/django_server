from ..shared_functions import *
from django.shortcuts import render
from django.http import *

GITHUB_API_URL = 'https://api.github.com'


def home_view(request):
    return render(request, "repos_viewer/home.html")


def user_view(req, name):
    print(f"got request: {req.path}")

    request = requests.get(GITHUB_API_URL + '/users/' + name + '/repos?per_page=100')

    if request.status_code == 404:
        return HttpResponse(content=render(request, "repos_viewer/error404.html"),
                            content_type='text/html; charset=utf-8',
                            status=404)
    if request.status_code == 500:
        return HttpResponse(content=render(request, "repos_viewer/error500.html"),
                            content_type='text/html; charset=utf-8',
                            status=500)
    if request.status_code == 403:
        return HttpResponse("api requests limit reached", status=403)

    repos_list_json, sum_of_stars = getAllReposOfUser(name, request)

    return render(req, "repos_viewer/user.html",
                  {"user_name": name, "json_list": repos_list_json, "sum_of_stars": sum_of_stars})
