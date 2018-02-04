# Python3 Flask Rest API with Celery example

## Installation

Note : The installation into a virtualenv is heavily recommended.

If you want to install the package :

```
pip install .
```

For development purposes, you can install the package in editable mode with the dev requirements.

```
pip install -e . -r requirements-dev.txt
```

## Usage

To start the application, you can use the file run.py :

```
python run.py
```

Moreover, to be able to play with celery, you have to first start Redis, then start a celery worker like this :

```
celery -A run.celery worker --loglevel=info
```

Note : It's cleaner to use docker-compose to start the whole application (see the section below).

## Usage with Docker Compose

In order to start the whole system easily, we can use docker-compose :

```
docker-compose up
```

It will start three docker containers :
- Redis
- Flask API
- Celery Worker

Then, you can access to the API in localhost :

```
curl -X GET -H "Content-Type: application/json" localhost:5000/api/bye/test
```

## Syntax

You can check the syntax using pylama (you must have pylama package installed first) :

```
pylama api
```

You can also use tox (you must have tox package installed first) :

```
tox -e pylama
```

## Test coverage

To execute the test coverage, you must install the package with the dev requirements (see installation section).

Note : You must start redis in localhost in order to pass de tests :

```
docker run -p 6379:6379 redis:latest
```

Then, you can run the coverage with the following command :

```
coverage run --source api -m py.test
```

You can also use tox (you must have tox package installed first) :

```
tox -e test
```
