import json
from datetime import datetime


def get_data_json(path):
    """
    функция для чтения файла .json
    """
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def get_executed_operations(operations):
    """
    Функция получает на вход список со словарями и формирует
    новый список с операциями executed
    """
    executed_operations = []
    for operation in operations:
        if operation.get('state') == "EXECUTED" and 'from' in operation:
            executed_operations.append(operation)
    return executed_operations


def sort_operations(operations):
    """
    Функция сортирующая операции EXECUTED по дате убывания
    """
    return sorted(operations, key=lambda operation: operation.get("date"), reverse=True)


def get_lats_operations(operations: list[dict], count=5):
    """
    Функция обрезающая колличество операций до необходимого колличества по заданию
    """
    return operations[:count]


def convert_date(date_str):
    """
    Функция конвертирующая дату
    """
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")


def convert_payment_info(payment_info):
    if payment_info.startswith('Счет'):
        return payment_info[:5] + '**' + payment_info[-4:]
    else:
        payment_list = payment_info.split()
        number = payment_list.pop()
        return ' '.join(payment_list) + ' ' + number[:4] + ' ' + number[4:6] + '** **** ' + number[-4:]
