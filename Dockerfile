FROM python:3.10

# Nao utilizar arquivos .pyc na construção da image/criação do container
ENV PYTHONDONTWRITEBYTECODE 1

# Os logs de erro não se perdem entre a aplicação e o container
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . /code/

RUN pip install -U pip
RUN pip install -r requirements.txt

