from subprocess import call

from os.path import join

def docker_build(path, name, dockerfile='Dockerfile'):
    args = [
        'docker',
        'build',
        '--tag',
        name,
        '--file',
        join(path, dockerfile),
        path
    ]
    call(args)
