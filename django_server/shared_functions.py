import re
import requests

GITHUB_API_URL = 'https://api.github.com'


def getRepoStars(user_name, repo_name, request):
    return request.json()['stargazers_count']


def getAllReposOfUser(user_name: str, request) -> (list, int):
    repos_list_json = []
    repos_list_json += request.json()

    if 'link' in request.headers:
        next_link = request.headers['link'].split(";", maxsplit=1)[0][1:-2]
        last_page = re.findall("page=(\d+)", next_link)[-1]
        for i in range(2, int(last_page) + 1):
            request = requests.get(next_link + str(i))
            repos_list_json += request.json()

    sum_of_stars = 0
    for repo in repos_list_json:
        sum_of_stars += repo['stargazers_count']

    return repos_list_json, sum_of_stars
