FROM python:3.9.0

WORKDIR /app
ARG requirements=requirements/production.txt

ADD . /app

RUN pip install --no-cache-dir -e .
RUN pip install --no-cache-dir -r $requirements
