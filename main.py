# -*- coding=utf-8 -*-

from prefs.config import BOT, \
                         LOG, \
                         SETTINGS, \
                         ADMINS, \
                         SEARCHES, \
                         EXTENSIONS, \
                         SNAPSHOTS
from src.logging import write_to_incoming_log
from src.request_helper import request_processing
from src.c_update import command_update, update_settings
from src.c_help import command_help

LOG.info('up')
update_settings()


@BOT.message_handler(SEARCHES)
def start_search(message):
    """
    Команды пользователей с аргуметами
    """
    if message.chat.id > 0:
        LOG.info('search')
        write_to_incoming_log(message)
        request_processing(message, SEARCHES)


@BOT.message_handler(['update'])
def start_update(message):
    if message.chat.id > 0:
        if int(message.from_user.id) in ADMINS:
            """
            Обноввить список команд
            """
            print('Update')
            write_to_incoming_log(message)
            command_update(message)


@BOT.message_handler(func=lambda m: True)
def start_help(message):
    """
    Генератор помощи
    """
    if str(message.text)[0] == '/':
        write_to_incoming_log(message)
        command_help(message)


BOT.infinity_polling(True)
