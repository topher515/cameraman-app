FROM ubuntu:14.04

MAINTAINER Chris Wilcox <ckwilcox@gmail.com>

WORKDIR /opt/devwebapp/app-server

# RUN apt-get update
# RUN apt-get install -y libxslt-dev libxml2-dev
# RUN apt-get -y install python python-dev python-pip build-essential git
# RUN apt-get -y install curl

RUN apt-get update
RUN apt-get install -y libxslt-dev libxml2-dev
RUN apt-get -y install python python-dev python-pip build-essential git
RUN apt-get -y install libpq-dev python-dev
RUN easy_install -U pip
RUN apt-get -y install postgresql-client

ADD requirements.txt requirements.txt

# Web app
RUN pip install -r requirements.txt

ADD setup.py setup.py

RUN python setup.py develop