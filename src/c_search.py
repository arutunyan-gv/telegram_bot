# -*- coding=utf-8 -*-

from prefs.config import EXECUTION_LOG_QUERY, \
                         EXECUTION_MAIN_QUERY, \
                         SNAPSHOTS
from src.db_helper import run_query_ro
from src.logging import write_to_error_log, \
                        write_to_outgoing_log
from src.telegram_helper import reply_func


def snapshot_name(exec_id):
    stage_id = run_query_ro('select stage_id from execution where id = ' + str(exec_id) + ';')[0]
    snapshot = run_query_ro('''	
                            select distinct m2.table_name snap_shop from stage s
                            join issue_type it on s.issue_type_id = it.id
                            join md_entity m2 on it.fact_table_id = m2.id
                            where s.id = 
                            ''' + str(stage_id[0]) + ';')
    return str(snapshot[0][0])


def create_ymap_link(exec_id, snapshot):
    try:
        location_id = \
            run_query_ro('select location_id from ' + snapshot + ' where execution_id = ' + exec_id)[0]
        map_link = run_query_ro(
            'select * from tmp.bot_location_map_link(' + str(location_id[0]) + ');')
    except Exception as val_err:
        write_to_error_log(msg='Не удалось получить ссылку на карту', error=val_err)
        map_link = ''
    if map_link:
        return '🗺 [Ссылка на карту](' + str(map_link[0][0]) + ')'
    else:
        return ''


def incorporate_reply(table, header='', plug=''):
    reply = ''
    if table:
        for row in table:
            if row:
                for sell in row:
                    if sell:
                        reply += str(sell)
    if not reply:
        return plug
    elif header:
        return header + '\n' + reply
    else:
        return reply


def execution_processing(message, execution):
    """
    Собираем данные по заданию
    """
    reply = ''
    snapshot = snapshot_name(execution)
    try:
        reply += incorporate_reply(
            run_query_ro(
                EXECUTION_MAIN_QUERY.replace('__arg__', execution)))
    except Exception as val_err:
        write_to_error_log(msg='Не удалось получить основные данные по заданию',
                           error=val_err)
    try:
        reply += '\n' + incorporate_reply(
            run_query_ro(
                EXECUTION_LOG_QUERY.replace('__arg__', execution)),
            header='🗒 Лог задания:',
            plug='🗒 Лог задания пуст.\n')
    except Exception as val_err:
        write_to_error_log(msg='Не удалось получить данные из execution_log:',
                           error=val_err)
    try:
        if snapshot in SNAPSHOTS:
            reply += '\n' + incorporate_reply(
                run_query_ro(SNAPSHOTS[snapshot][0].replace('__arg__', execution)),
                plug='💾 Дополнительные данные по заданию недоступны.\n')
    except Exception as val_err:
        write_to_error_log(msg='Не удалось получить данные из снапшота:',
                           error=val_err)
    try:
        reply += '\n' + create_ymap_link(execution, snapshot)
    except Exception as val_err:
        write_to_error_log(msg='Не удалось получить ссылку на карту',
                           error=val_err)

    write_to_outgoing_log(message, reply)
    reply_func(message, reply)
