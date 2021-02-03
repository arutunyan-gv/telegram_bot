# -*- coding=utf-8 -*-

import logging
from src.db_helper import run_query_rw
from prefs.config import APP_NAME, \
                         INCOMING_LOG_QUERY, \
                         OUTGOING_LOG_QUERY, \
                         ERROR_LOG_QUERY, \
                         LOG


def query_attr_update(query, message, reply=''):
    return query.format(
        str(message.message_id),
        str(message.from_user.id),
        str(message.from_user.username),
        str(message.from_user.first_name) + ' ' + str(message.from_user.last_name),
        str(message.chat.id),
        str(message.chat.title),
        str(message.text.split(' ')[0]),
        str(reply if reply else message.text),
        str(APP_NAME))


def write_to_incoming_log(message):
    return run_query_rw(query_attr_update(INCOMING_LOG_QUERY, message))


def write_to_outgoing_log(message, reply):
    return run_query_rw(query_attr_update(OUTGOING_LOG_QUERY, message, reply=reply))


def write_to_error_log(msg='', data='', error='', messege_id=None):
    if msg:
        LOG.info(msg)
    if error:
        LOG.exception(error)
    query = ERROR_LOG_QUERY.format(
        str(msg).replace("'", "\\'"),
        str(data).replace("'", "\\'"),
        str(error).replace("'", "\\'"),
        messege_id if messege_id else 'null::bigint',
        str(APP_NAME))
    return run_query_rw(query)