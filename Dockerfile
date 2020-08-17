ARG PYTHON_VERSION=3.8.2
FROM python:${PYTHON_VERSION}-slim-buster as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

EXPOSE 8000

CMD ["python", "run.py"]

