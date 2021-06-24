FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN apt-get update
RUN apt-get install python3-dev mariadb-server libssl-dev default-libmysqlclient-dev gcc  -y
RUN mkdir /code
WORKDIR /code
ADD requirements.txt \
    /code/
RUN pip3 install -r requirements.txt
ADD . /code/
RUN useradd -m app
USER app