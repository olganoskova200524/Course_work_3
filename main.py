from config import OPERATIONS_JSON_PATH
from src.utils import get_data_json, get_executed_operations, sort_operations, get_lats_operations, convert_date, \
    convert_payment_info


def main():
    """
    Запуск программы
    """
    operations = get_data_json(OPERATIONS_JSON_PATH)
    executed_operations = get_executed_operations(operations)
    sorted_operations = sort_operations(executed_operations)
    lats_operations = get_lats_operations(sorted_operations)
    for operation in lats_operations:
        converted_date = convert_date(operation.get('date'))
        converted_payment_from = convert_payment_info(operation.get('from'))
        converted_payment_to = convert_payment_info(operation.get('to'))

        result = (f"{converted_date} {operation['description']}\n"
                  f"{converted_payment_from} -> {converted_payment_to}\n"
                  f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n")
        print(result)


main()
