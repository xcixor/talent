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
# COPY ./requirements.txt .
# RUN pip install --upgrade pip -r requirements.txt

# db healthcheck
COPY ./scripts/postgres-healthcheck.py /usr/local/bin/postgres-healthcheck
RUN chmod u+x /usr/local/bin/postgres-healthcheck

# create directory for the app user
RUN mkdir -p /home/app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/talent
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# copy entrypoint-prod.sh
COPY ./scripts/entrypoint.prod.sh $APP_HOME
RUN chmod u+x $APP_HOME/entrypoint.prod.sh

# copy project
COPY ./app $APP_HOME
ARG PORT

ENTRYPOINT ["/home/app/talent/entrypoint.prod.sh"]
