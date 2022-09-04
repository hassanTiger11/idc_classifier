FROM python:3.8-slim
ARG port

USER root
COPY . /app
WORKDIR /app

ENV PORT=$port

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils \
    && apt-get -y install curl \
    && apt-get install libgomp1

RUN chgrp -R 0 /app \
    && chmod -R g=u /app \
    && cd app && python3 -m venv .venv && ls -r .venv &&source ./.venv/bin/activate \
    && pip install pip --upgrade \
    && pip install -r requirements.txt
EXPOSE $PORT

CMD cd app && gunicorn app:server --bind 0.0.0.0:$PORT --preload