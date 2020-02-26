# Caide on docker

This tool is a wrapper of [caide](https://github.com/slycelote/caide) specifically to build solutions that uses multiple includes.

## Install

1. Install [docker](https://docs.docker.com/install/)

2. Build the docker image from the Dockerfile:

    ```bash
    cd /path/to/caide-docker
    docker build . -t caide-docker
    ```

3. Subsequently you will need to invoke the python script `caide.py`. Optionally you can add it to your path.

    ```bash
    sudo ln -s (pwd)/caide.py /usr/local/bin/caide-docker
    ```

## Create submission

In the example folder try:

```bash
caide-docker solution.cpp -l library -o main.cpp
```
