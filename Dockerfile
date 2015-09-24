FROM python:3.5

RUN sh -c 'curl -L https://get.docker.com/builds/$(uname -s)/$(uname -m)/docker-latest' > /usr/local/bin/docker
RUN chmod +x /usr/local/bin/docker

RUN pip install \
    Flask \
    gitpython
