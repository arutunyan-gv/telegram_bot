# -*- coding=utf-8 -*-

import re
from src.telegram_helper import reply_func
from src.db_helper import run_query_ro
from src.logging import write_to_error_log
from src.c_search import execution_processing


def query_split(query):
    """
    Разделяет запрос пользователя на аргументы.
    """
    for_replace = [',', '\t', '\n']
    i = 0
    while i < len(for_replace):
        query = query.replace(for_replace[i], ' ')
        i += 1
    while '  ' in query:
        query = query.replace('  ', ' ')
    query = query.split(' ')
    return query


def request_processing(message, queries):
    """
    Получаем номера заданий из запроса.
    """
    args = query_split(message.text)
    command = args[0].replace('/', '')
    args.pop(0)

    if args:
        for arg in args:
            try:
                arr = run_query_ro(str(queries[command][0]).replace('__arg__', arg))
            except Exception as val_err:
                write_to_error_log(msg='Выполнение запроса завершилось ошибкой:', error=val_err)
                return None
            if arr:
                for execution in arr:
                    exec_id = str(execution[0])
                    if re.match('^[0-9]+$', exec_id):
                        execution_processing(message, exec_id)
                    else:
                        reply_func(message, 'Ничего не удалось найти по запросу:\n\n`' + exec_id + '`')
            else:
                reply_func(message, 'Ничего не удалось найти по запросу:\n\n`' + arg + '`')
    else:
        reply_func(message, 'Необходимо ввести хотя бы одни аргумент.\nК примеру:\n\n`/knd 12345`')
