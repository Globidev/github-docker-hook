from lib.git import clone_tmp
from lib.docker import docker_build

ROUTE = '/push'
PORT = 4242

def on_push(data):
    url = data['repository']['html_url']
    with clone_tmp(url) as repo:
        docker_build(repo.path, 'github-hook')
