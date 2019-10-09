FROM python:3.7.4-alpine3.9
LABEL maintainer "ryuichi1208 <ryucrosskey@gmail.com>"

WORKDIR /home/api
COPY --chown=root:root requirements.txt /home/api

ENV PYTHON_VERSION=3.7.4 \
    PY-DEP-KUN_VERSION=1.0.0 \
    LANG=C.UTF-8 \
    TZ=Asia/Tokyo \
    PYTHONUNBUFFERED=1

RUN apk --update-cache --no-cache \
    add musl \
    linux-headers \
    gcc \
    g++ \
    make \
    gfortran \
    openblas-dev \
    bash bash-completion \
    && python -m venv py-dep-kun \
    && . py-dep-kun/bin/activate \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

