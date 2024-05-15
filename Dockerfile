FROM python:3.8

WORKDIR /app

ADD . /app

RUN pip install --no-cache-dir flask

EXPOSE 5000

CMD ["python", "servicio-flask.py"]