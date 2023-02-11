# E-commerce

Simple e-commerce backend with Django and Django Rest Framework.

## Documentation

The documentation is available [here](https://documenter.getpostman.com/view/16429730/2s935uFfeD).

## Docker

You can run the project with docker.

```bash
docker build -t e-commerce .
docker run -p 8000:8000 e-commerce
```

## Installation

1. Clone the repository

2. Create a virtual environment

3. Install the requirements

```bash
pip install -r requirements.txt
```

4. Run the migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser

```bash
python manage.py createsuperuser
```

6. Run the server

```bash
python manage.py runserver
```
