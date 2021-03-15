FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1
MAINTAINER StudentsSystem


RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y apt-utils
RUN apt-get install gcc -y
RUN apt-get clean \
RUN apt-get install -y python-setuptools
RUN apt-get install -y libpq-dev python3-dev
RUN apt-get install -y systemd

COPY CodeSchoolAPI/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . StudentsSystem/

EXPOSE 8030

CMD ["python3", "CodeSchoolAPI/manage.py", "runserver", "0.0.0.0:8030"]
