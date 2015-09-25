from lib.git import clone_tmp
from lib.docker import build, push

ROUTE = '/push'
PORT = 4242

IMAGE_NAME = 'globidocker/github-hook'

def on_push(data):
    url = data['repository']['html_url']

    with clone_tmp(url) as repo:
        build(repo.path, IMAGE_NAME)
        push(IMAGE_NAME)
