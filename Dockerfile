FROM python:3.10.16-slim-bullseye

RUN apt-get update

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/app"
ENV PYTHONUNBUFFERED 1

ENTRYPOINT ["python3"]