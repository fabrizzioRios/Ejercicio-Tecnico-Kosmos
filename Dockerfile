FROM python:3.10-alpine
LABEL authors='Fabrizzio Rios'

WORKDIR /app

COPY tcp_server_kosmos.py /app
COPY tcp_client_kosmos.py /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1
