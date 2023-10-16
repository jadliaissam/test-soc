# Test API for S***tec

## Features

The project is a simple CRUD API for managing movies, actors and reviews. It includes the following features:

- RESTFull API for managing movies, actors and reviews
- Asynchronous task processing using Celery and Redis
- Docker Compose setup for easy deployment
- Unit tests for all endpoints
- Gunicorn as WSGI server
- API documentation using Swagger

## Requirements

The requirements used to run the project are:

- Python 3.11
- Django 4.2.6
- Celery 5.3.4
- Redis 7
- Docker
- Docker Compose

### Running the project

P.S : if you need to run the project without docker,
you may need to set the environment variable for redis connection.

```shell
CELERY_BROKER_URL=redis://localhost:6379/0
```

Clone the repository to your local machine:

```shell
git clone https://github.com/jadliaissam/test-soc.git
```

Change directory to the project root:

```shell
cd test-soc
```

Run the project using docker-compose:

```shell
docker-compose up --build -d
```

The API will be available at http://localhost:8000

### Running the tests

To run the tests, run the following command:

```shell
python manage.py test cine.tests
```

### API Documentation

The API documentation is available at http://localhost:8000/swagger/
