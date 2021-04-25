# Github User and Repository viewer

## Setup

Clone repository:

    git clone https://github.com/AdamOsiowy/django_server.git
    cd django_server

Create virtual environment and activate it:

    pip install virtualenv
    virtualenv venv
    source venv/bin/activate

Install dependencies:

    pip install -r requirements.txt

Run server:

    cd django_server
    python manage.py runserver

Then open browser at home page: `http://127.0.0.1:8000/`

## Description
It's a web server wrote in Django with its own RESTapi that enables you to:
- list repository (name and stars)
- list user (name, sum of stars and highlights of his public repositories)

Data is returned via http protocol.

## Examples

Urls pattern: \
`http://127.0.0.1:8000/{username}` \
`http://127.0.0.1:8000/{username}/{repo_name}` \
Endpoints: \
`http://127.0.0.1:8000/api/{username}` \
`http://127.0.0.1:8000/api/{username}/{repo_name}` 

- to list user named AdamOsiowy \
    open http://127.0.0.1:8000/AdamOsiowy \
    or run in terminal: \
    `curl -i -H "Accept: application/json" http://127.0.0.1:8000/api/AdamOsiowy`


- to get information about AdamOsiowy repository named Screenshotter:
    open http://127.0.0.1:8000/AdamOsiowy/Screenshotter \
    or run in terminal: \
    `curl -i -H "Accept: application/json" http://127.0.0.1:8000/api/AdamOsiowy/Screenshotter`

You can do that for all Github users even if they have more than 1k repositories.

## Next steps:
- improve the homepage to include a description of the project
- use created models to store data in database
- setup docker and CI/CD
- add POST method support to create repositories via GitHub api
- improve user and repository pages to contain more informations
- add tests to check the operation correctness of the server
