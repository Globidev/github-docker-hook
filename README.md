# github-docker-hook
A post push github hook to generate docker images and/or do other cool stuff

### Usage
1. On your server, where docker is obviously installed, login to your image server:
 ```sh
 docker login
 ```

2. Write your hook logic by creating a python file `awesome_hook.py` that looks like this:
 ```python
 ROUTE = '/some_route'
 PORT = 4242 # Or some other port

 def on_push(json_payload, logger):
      # Do something when someone pushes to your repository
 ```
 :information_source: You can find the hook used for this very repository [here](example/my_hook.py)

3. Setup a github webhook for your repository in the settings:
 ![webhook](https://cloud.githubusercontent.com/assets/2079561/10090442/bc5479ba-632f-11e5-82f1-ff7baa6a8286.png)

4. Create a simple derivate Dockerfile for your project:
 ```dockerfile
 FROM globidocker/github-hook
 
 ADD awesome_hook.py /hook/
 ```
 and build it:
 ```sh
 docker build -t my-app-hook .
 ```

5. Run the hook server:
 ```sh
 docker run \
      --detach \
      --name my-app-hook-server \
      -v /var/run/docker.sock:/var/run/docker.sock \
      -v $HOME/.docker:/root/.docker \
      -p 4242:4242  \
      my-app-hook \
      awesome_hook
 ```
