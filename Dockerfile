FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1
WORKDIR /zxc
COPY requirements.txt /zxc/requirements.txt

RUN pip install -r /zxc/requirements.txt


COPY . .