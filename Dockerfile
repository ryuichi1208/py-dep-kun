FROM python:3.7.4-alpine3.9
LABEL maintainer "ryuichi1208 <ryucrosskey@gmail.com>"

WORKDIR /home/api
COPY . /home/api

ENTRYPOINT [ "pwd" ]

