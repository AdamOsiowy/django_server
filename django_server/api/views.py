from django.http import HttpResponse, HttpResponseNotAllowed
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from .models import User, Repository
from .serializer import UserSerializer, RepositorySerializer
import json
from ..shared_functions import *

GITHUB_API_URL = 'https://api.github.com'


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RepositoryViewSet(viewsets.ModelViewSet):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer


@api_view(['GET', ])
def get_user_view(req, name):
    request = requests.get(GITHUB_API_URL + '/users/' + name + '/repos?per_page=100')
    if request.status_code == 404:
        return HttpResponse(json.dumps({"error_code": 404}), content_type="application/json", status=404)
    if request.status_code == 500:
        return HttpResponse(json.dumps({"error_code": 500}), content_type="application/json", status=500)
    if request.status_code == 403:
        return HttpResponse(json.dumps({"error_code": 403}), content_type="application/json", status=403)

    sum_of_stars = getAllReposOfUser(name, request)[1]

    if req.method == "GET":
        return HttpResponse(json.dumps({"user_name": name, "sum_of_stars": sum_of_stars}),
                            content_type="application/json", status=200)
    else:
        return HttpResponseNotAllowed("GET")


@api_view(['GET', ])
def get_repo_view(req, name, repo_name):
    request = requests.get(GITHUB_API_URL + '/repos/' + name + '/' + repo_name)

    if request.status_code == 404:
        return HttpResponse(json.dumps({"error_code": 404}), content_type="application/json", status=404)
    if request.status_code == 500:
        return HttpResponse(json.dumps({"error_code": 500}), content_type="application/json", status=500)
    if request.status_code == 403:
        return HttpResponse(json.dumps({"error_code": 403}), content_type="application/json", status=403)

    stars = getRepoStars(name, repo_name, request)
    if req.method == "GET":
        return HttpResponse(json.dumps({"repo_name": repo_name, "stars": stars}), content_type="application/json",
                            status=200)
    else:
        return HttpResponseNotAllowed("GET")
