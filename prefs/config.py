# -*- coding=utf-8 -*-

import os
import telebot
import logging
# from src.queries_helper import read_queries
from src.service import read_file

# logging.basicConfig(filename="sample.log", level=logging.INFO)
LOG = logging.getLogger("ex")

APP_NAME = os.environ.get('APP_NAME')

# Аутентификация в Postgres
DB_NAME = os.environ.get('DB_NAME')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_APP_NAME = os.environ.get('DB_APP_NAME')

# Подключение к телеграм
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
BOT = telebot.TeleBot(TELEGRAM_TOKEN)

SETTINGS = {}
ADMINS = {}
SEARCHES = {}
EXTENSIONS = {}
SNAPSHOTS = {}

QUERY_EXTENSION = '.sql'

# Запросы для логирования
PATH_LOGGING = 'src/queries/logging/'
INCOMING_LOG_QUERY = read_file(PATH_LOGGING + 'incoming' + QUERY_EXTENSION)
OUTGOING_LOG_QUERY = read_file(PATH_LOGGING + 'outgoing' + QUERY_EXTENSION)
ERROR_LOG_QUERY = read_file(PATH_LOGGING + 'error' + QUERY_EXTENSION)


# Запросы по сбору данных из задания
PATH_EXECUTION = 'src/queries/execution/'
EXECUTION_LOG_QUERY = read_file (PATH_EXECUTION + 'log' + QUERY_EXTENSION)
EXECUTION_MAIN_QUERY = read_file (PATH_EXECUTION + 'main' + QUERY_EXTENSION)
EXECUTION_MAP_QUERY = read_file (PATH_EXECUTION + 'map' + QUERY_EXTENSION)
