FROM python:3.10.9

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

# Copy project

COPY . .

# Run migrations

RUN python manage.py makemigrations

RUN python manage.py migrate

RUN python manage.py shell -c "import seed"

# Run server

CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]
