# Python3 Flask Rest API skeleton

## Installation

If you want to install the package :

```
pip install .
```

You can also directly install the package with the dev requirements :

```
pip install . -r requirements-dev.txt
```

Note : You may want to install it in a virtual environment.

## Usage

To start the application, you can use the file run.py :

```
python run.py
```

Then, you can access to the api in localhost :

```
curl -X GET -H "Content-Type: application/json" localhost:5000/api/hello/test
```

## Usage with Docker

To use it in a Docker container, just build it :

```
docker build -t myapi .
```

Then run it :

```
docker run -p 127.0.0.1:5000:80 myapi
```

## Syntax

You can check the syntax using pylint (you must have pylint package installed first) :

```
pylint --rcfile=setup.cfg api
```

Or with tox (you must have tox package installed first) :

```
tox -e pylint
```

## Coverage

To see the test coverage, you must install the package with the dev requirements (see installation section).

Then, you can run the coverage with the following command :

```
coverage run --source api -m py.test
```

Or with tox (you must have tox package installed first) :

```
tox -e pytest
```
