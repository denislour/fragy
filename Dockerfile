# pull official base image
FROM python:3.7.5-slim-buster

# set work directory
WORKDIR /pallets

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
ENTRYPOINT ["sh", "/pallets/entrypoint.sh"]
