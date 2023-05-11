# pull base image
FROM python:3.10

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install dependencies
COPY Pipfile Pipfile.lock ./
RUN pip install --upgrade pip pipenv && pipenv install --system

# db healthcheck
COPY ./scripts/postgres-healthcheck.py /usr/local/bin/postgres-healthcheck
RUN chmod u+x /usr/local/bin/postgres-healthcheck

# copy entrypoint-prod.sh
COPY ./scripts/entrypoint.prod.sh /usr/src/app
RUN chmod u+x /usr/src/app/entrypoint.prod.sh

# copy project
COPY ./app .

ARG PORT

ENTRYPOINT ["/home/app/talent/entrypoint.prod.sh"]