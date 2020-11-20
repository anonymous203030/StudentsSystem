FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1
MAINTAINER StudentsSystem


RUN apt-get update -y \
&& apt-get upgrade -y \
&& apt-get install -y apt-utils \
&& apt-get install gcc -y \
&& apt-get clean \
&& apt-get install -y python-setuptools \
&& apt-get install -y libpq-dev python3-dev \
&& apt-get install -y systemd

RUN mkdir /StudentsSystem
WORKDIR /StudentsSystem
COPY ./CodeSchoolAPI ./StudentsSystem

COPY CodeSchoolAPI/requirements.txt /requirements.txt

RUN pip3 install -r StudentsSystem/requirements.txt