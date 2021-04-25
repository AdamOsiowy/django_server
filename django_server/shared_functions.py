GITHUB_API_URL = 'https://api.github.com'


def getRepoStars(user_name, repo_name, request):
    return request.json()['stargazers_count']
