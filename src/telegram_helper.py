# -*- coding=utf-8 -*-

import time

from prefs.config import BOT
from src.logging import write_to_outgoing_log, \
                        write_to_error_log


def reply_func(message, reply):
    """
    Ответ пользователю.
    :param message:
    :param reply:
    :return:
    """
    reply = str(reply)
    try:
        BOT.reply_to(message, reply, parse_mode='Markdown')
    except ValueError as val_err:
        write_to_error_log(msg='reply_func - error:', error=val_err, data=message)
    try:
        write_to_outgoing_log(message, reply)
    except ValueError as val_err:
        write_to_error_log(msg='reply_func - error:', error=val_err, data=message)
    time.sleep(2)

