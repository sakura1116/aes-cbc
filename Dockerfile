FROM python:3.8.2-buster

ARG pipenv_install_option="--system --dev"

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

RUN set -eux; \
  apt-get update; \
  apt-get install -y --no-install-recommends \
    vim \
    git \
    jq \
    unzip \
    make

RUN pip3 install pipenv
WORKDIR /opt/sakura

ENV PYTHONPATH /opt/sakura/src

COPY ./Pipfile ./
COPY ./Pipfile.lock .
RUN pipenv install $pipenv_install_option

COPY ./src ./src
