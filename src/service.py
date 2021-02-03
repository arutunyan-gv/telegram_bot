# -*- coding=utf-8 -*-


def read_file(file_name):
    """
    Чтение файла в строку
    """
    reply = ''
    with open(str(file_name), 'r') as file:
        for line in file:
            reply = reply + line
        file.close()
    return str(reply)



