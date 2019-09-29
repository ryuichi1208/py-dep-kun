FROM python:3.7.4-alpine3.9
LABEL maintainer "ryuichi1208 <ryucrosskey@gmail.com>"

WORKDIR /home/api
COPY . /home/api

ENTRYPOINT [ "pwd" ]

RUN apk add --no-cache ca-certificates && update-ca-certificates
ADD https://get.aquasec.com/microscanner .
RUN chmod +x microscanner
