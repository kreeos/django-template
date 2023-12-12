# syntax=docker/dockerfile:1.3

FROM python:3.11.7-slim

WORKDIR /app

RUN apt-get -qq update && \
    apt-get install -y --no-install-recommends \
      wget \
      git \
      g++ \
      libgeos-dev \
      libgmp3-dev \
      libpq-dev \
      libmaxminddb-dev && \
  rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock ./
RUN poetry install

ADD --chown=app:app . .
USER app

COPY . /app/
