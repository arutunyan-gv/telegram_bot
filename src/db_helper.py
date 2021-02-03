# -*- coding=utf-8 -*-
import psycopg2
from prefs.config import DB_NAME, \
                         DB_HOST, \
                         DB_PASS, \
                         DB_PORT, \
                         DB_USER, \
                         DB_APP_NAME


def db_connect():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASS,
        application_name=DB_APP_NAME,
    )
    return conn


def run_query(commit, query):
    try:
        conn = db_connect()
        cursor = conn.cursor()
        conn.autocommit = commit
    except Exception as val_err:
        print('Не удалось подключится к базе данных:')
        print(val_err)

    try:
        cursor.execute(query)
    except Exception as val_err:
        print('Не удалось выполнить запрос:')
        print(val_err)
        print(query)

    try:
        res = cursor.fetchall()
    except Exception as ex:
        res = None

    try:
        cursor.close()
        conn.close()
    except Exception as val_err:
        print('Не удалось закрыть подключение к базе данных')
        print(val_err)

    return res


def run_query_ro(query):
    return run_query(True, query)


def run_query_rw(query):
    return run_query(True, query)