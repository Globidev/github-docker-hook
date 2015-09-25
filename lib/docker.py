from subprocess import call

from os.path import join

def build(path, name, dockerfile='Dockerfile'):
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
