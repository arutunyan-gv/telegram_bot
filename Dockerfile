FROM python:3.8-slim

LABEL key="Georgiy Arutunyan <liquid245+mincraft@gmail.com>"

ENV DEBIAN_FRONTEND noninteractive
ENV LANGUAGE ru_RU.UTF-8
ENV LANG ru_RU.UTF-8
ENV LC_ALL ru_RU.UTF-8



RUN set -xe && \
    apt-get -qqy update && \
    apt-get install -qqy --no-install-recommends \
    locales \
    && \
    sed -i -e 's/# ru_RU.UTF-8 UTF-8/ru_RU.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure locales && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/cache/apt && \
    :

RUN python -m pip install --upgrade pip
RUN pip3 install \
    psycopg2-binary \
    telebot \
    pyTelegramBotApi \
    statistics \
    ;
RUN pip3 install --upgrade certifi

COPY . ./app

WORKDIR /app

RUN chmod 777 main.py
CMD python main.py

