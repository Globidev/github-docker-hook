FROM python:3.5

RUN sh -c 'curl -L https://get.docker.com/builds/$(uname -s)/$(uname -m)/docker-latest' > /usr/local/bin/docker
RUN chmod +x /usr/local/bin/docker

RUN pip install \
    Flask \
    gitpython \
    docker-py

ADD lib/ /hook/lib
ADD main.py /hook/
ADD example/my_hook.py /hook/
WORKDIR /hook

ENTRYPOINT ["python", "main.py"]
