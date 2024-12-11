FROM  python:3.12.5-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /usr/src/app
RUN mkdir -p $WORKDIR/static
RUN mkdir -p $WORKDIR/media

RUN pip install --upgrade pip

COPY ./src/requirements.txt src/
COPY ./src/requirements-dev.txt src/
RUN pip install -r src/requirements.txt -r src/requirements-dev.txt

COPY . .
