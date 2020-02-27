# Caide on docker

This tool is a wrapper of [caide](https://github.com/slycelote/caide) specifically to build solutions that uses multiple includes.

## Install

1. Install [docker](https://docs.docker.com/install/)

2. Build the docker image from the Dockerfile:

    ```bash
    cd /path/to/caide-docker
    docker build . -t caide-docker
    ```

3. All interaction is done via the python script `caide.py`. To invoke this script use: `python3 /path/to/caide.py` or create an alias:

    ```bash
    sudo ln -s $(pwd)/caide.py /usr/local/bin/caide-docker
    ```

You are ready to go. Use `caide-docker --help` to see the options.

## Usage

In the `example` folder try:

```bash
caide-docker solution.cpp -l library -o main.cpp
```
