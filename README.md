

![Docker Image CI](https://github.com/TheForeverLost/FlaskAPIDocker/workflows/Docker%20Image%20CI/badge.svg?branch=master)

# FlaskAPIDocker

Flask API package skeleton ideal for microservices using docker

This template is a variation by one provided by [Sebastian Ramirez](https://github.com/tiangolo)

### Usage

The application runs with the help of the base image offered by Sebastian :
[`uwsgi-nginx-flask:python3.8`](https://github.com/tiangolo/uwsgi-nginx-flask-docker/blob/master/docker-images/python3.8.dockerfile)

This image allows quick setup of a flask application with the help of nginx and uwsgi making a production ready container that you can quickly deploy to your clusters.

build:

```bash
$ docker build -t <image>:<tag>
```

run:

```bash
$ docker run -p 80:80 --name <container name> <image>:<tag>
```

or we could use docker compose

```bash
$ docker-compose up
```



### references

Do check out Sebastian Ramirez for more amazing docker images that you can use
Also check out [his medium blog](https://medium.com/@tiangolo)