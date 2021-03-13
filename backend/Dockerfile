FROM python:3.8-slim

WORKDIR /usr/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt .

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . .

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]