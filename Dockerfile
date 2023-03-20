# syntax=docker/dockerfile:1
# TODO при создании контейнера файл выложить в корневой каталог, туда же выложить requirements.txt

FROM python:3.11
WORKDIR /football_analytics

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY .. .

# команда для запуска (не актуальна)
# docker build ./utils/ -t doker_flsk
