from config import TEST_OPERATIONS_PATH
from src.utils import convert_payment_info, get_executed_operations, sort_operations, get_lats_operations, convert_date, \
    get_data_json


def test_get_data_json():
    operation = get_data_json(TEST_OPERATIONS_PATH)
    assert len(operation) == 3


def test_get_executed_operations(executed_operations_fixture, canceled_operations_fixture, operations_fixture):
    operation = get_executed_operations(executed_operations_fixture)
    assert len(operation) == 2
    operation = get_executed_operations(canceled_operations_fixture)
    assert len(operation) == 0
    operation = get_executed_operations(operations_fixture)
    assert len(operation) == 1


def test_sort_operations(operations_fixture):
    operation = sort_operations(operations_fixture)
    assert operation[0].get("date") == "2020-07-03T18:35:29.512364"
    assert operation[0].get("date") > operation[1].get("date")


def test_get_lats_operations(executed_operations_fixture, canceled_operations_fixture, operations_fixture):
    operation = get_lats_operations(executed_operations_fixture, count=1)
    assert operation
    operation = get_lats_operations(canceled_operations_fixture, count=4)
    assert operation


def test_convert_date():
    operation = convert_date(date_str="2020-06-30t15:11:53.136004")
    assert operation == "30.06.2020"
    operation = convert_date(date_str="2018-06-30t15:11:53.136004")
    assert operation == "30.06.2018"


def test_convert_payment_info(executed_operations_fixture, canceled_operations_fixture, operations_fixture):
    operation = convert_payment_info(payment_info="Счет 59956820797131895975")
    assert operation == "Счет **5975"
    operation = convert_payment_info(payment_info="Счет 43475624104328495820")
    assert operation == "Счет **5820"
