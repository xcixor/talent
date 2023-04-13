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

# copy project
COPY ./app .

ARG PORT

CMD python manage.py makemigrations; python manage.py migrate; python manage.py create_admin; python manage.py runserver 0.0.0.0:${PORT}