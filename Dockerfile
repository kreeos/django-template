# syntax=docker/dockerfile:1.3

FROM python:3.11.7-slim

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir

COPY . /app/
