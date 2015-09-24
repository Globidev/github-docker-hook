from tempfile import mkdtemp
from git import Repo
from shutil import rmtree

class Repository:

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def __enter__(self):
        self.repo = Repo.clone_from(self.url, self.path)
        return self

    def __exit__(self, *args):
        rmtree(self.path)

def clone_tmp(url):
    path = mkdtemp()
    return Repository(url, path)
