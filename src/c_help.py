# -*- coding=utf-8 -*-

from src.telegram_helper import reply_func
from prefs.config import SEARCHES, SNAPSHOTS, ADMINS, EXTENSIONS, SETTINGS


def content_len(content):
    length = 0
    for item in content:
        item_len = len(str(item))
        if item_len > length:
            length = item_len
    return length


def add_space(element, length):
    e_len = length - len(str(element))
    string = ''
    while e_len > 0:
        string += ' '
        e_len -= 1
    return string


def help_chapter(header, content, suffix='', new_line=False, row_num=-1):
    result = ''
    if new_line:
        length = 0
        nl = '\n'
    else:
        length = content_len(content)
        nl = ''
    for element in content:

        result += '  - `' + str(element) + add_space(element, length) + '`' + suffix + nl + str(content[element][row_num]) + '\n'
    return str('\n' + str(header) + '\n' + result)


def command_help(message):
    reply = '🤖 Бот ЕГИС ОКНД 🤖\n\n'

    if not ('/help' in str(message.text) or '/help' in str(message.text)):
        reply += 'Введена не верная команда.\n'

    if message.chat.id > 0:
        reply += 'Введите одну из приведенных ниже команд с аргументом.\n'
    else:
        reply += 'Бот принимает команды только в личном чате. Нажмите на ссылку:\n@moc\\_ict\\_bot\n'

    reply += help_chapter(
               '*Получение информации о задании:*', SEARCHES, suffix='  —  ')
    reply += '\nМаксимальное количество аргументов для одного запроса: ' + str(SETTINGS['max_args'][0]) + '\n'
    reply += 'Пример c двумя аргументами:\n`' + '/knd 12345, 23456' + '`\n'

    reply_func(message, reply)