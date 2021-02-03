# -*- coding=utf-8 -*-

from prefs.config import SEARCHES, SNAPSHOTS, SETTINGS, ADMINS, EXTENSIONS
from src.telegram_helper import reply_func
from src.db_helper import run_query_ro, run_query_rw
from src.c_help import help_chapter


def read_settings(dictionary, query):
    table = run_query_ro(query)
    commands = []
    queries = {}
    if table:
        for row in table:
            dictionary[row[0]] = [row[1], row[2]]


def chapter(header, content, prefix=''):
    result = ''
    elem = ''
    for element in content:
        try:
            elem = ': ' + str(content[element]) + ' '
        except:
            elem = ''
        result += '  - `' + prefix + str(element) + elem + '`\n'
    return str('\n' + str(header) + '\n' + result)


def update_settings():
    read_settings(SEARCHES,
                  'select command, query, description from bot.commands_searches order by command')
    read_settings(SNAPSHOTS,
                  'select snapshot_name, query, description from bot.addons_snapshot_info order by snapshot_name')
    read_settings(SETTINGS,
                  'select name, value, comment from bot.prefs_main order by name')
    read_settings(ADMINS,
                  'select user_id, username, name from bot.prefs_admins order by user_id')


def command_update(message):
    update_settings()
    reply = '🤖 Бот ЕГИС ОКНД 🤖\n'
    reply += help_chapter(
        '*Настройки:*', SETTINGS, suffix=':  ', row_num=0)
    reply_func(message, reply)
    reply = ''

    reply += help_chapter(
        '*Админимтраторы:*', ADMINS, suffix='  —  ')
    reply_func(message, reply)
    reply = ''

    reply += help_chapter(
        '*Поиск заданий:*', SEARCHES, suffix='  —  ')
    reply_func(message, reply)
    reply = ''

    reply += help_chapter(
        '*Снапшоты:*', SNAPSHOTS, suffix=':', new_line=True)
    reply_func(message, reply)
    reply = ''


