ROUTE = '/push'
PORT = 4242

IMAGE_NAME = 'globidocker/github-hook'

import docker

cli = docker.Client()

from lib.git import clone_tmp

def on_push(data, logger):
    url = data['repository']['html_url']

    logger.info('Cloning repository: "{}"...'.format(url))
    with clone_tmp(url) as repo:

        logger.info('Building image...')
        cli.build(repo.path, IMAGE_NAME)

        logger.info('Pushing image...')
        cli.push(IMAGE_NAME)

        logger.info('done')
