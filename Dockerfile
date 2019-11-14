FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3.7 \
    python3-requests \
    python3-pip

RUN rm /usr/bin/python3
RUN ln -s /usr/bin/python3.7 /usr/bin/python3
RUN pip3 install pyyaml flask flask_restful

COPY main.py /apps/main.py
RUN mkdir /apps

WORKDIR /apps
ENTRYPOINT tail -f /dev/null
