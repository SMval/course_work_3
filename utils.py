import json

# Константы
FILENAME = 'operations.json'


def get_operations():
    """Получение списков словарей из файла и их преобразование"""

    with open(FILENAME) as file:
        return json.load(file)


def sort_operations_by_date(list_operations):
    """ Сортировка списка словарей по дате """

    sorted_date = sorted(list_operations, key=lambda sort_operation: sort_operation.get('date', ''), reverse=True)
    return sorted_date


def get_five_executed(list_operations):
    """Получение 5 последних выполненных операций"""

    executed_list = []
    for data in list_operations:
        if data.get('state') == 'EXECUTED':
            executed_list.append(data)

    filter_list = executed_list[0:5]
    return filter_list


def get_data(list_operations):
    """Вывод 5 последних операций в формате:
    <дата перевода> <описание перевода>
    <откуда> -> <куда>
    <сумма перевода> <валюта>
    """

    # Список операций
    list_of_operations = []

    # Начало цикла
    for item in list_operations:
        slice_my_date = item['date'][:10].split('-')

        # Дата перевода
        filter_date = '.'.join(reversed(slice_my_date))

        # Описание перевода
        money_transfer = item['description']

        # Проверка наличия ключа 'from'
        if not item.get('from'):
            req_info_2 = item['to'].split()
            number_2 = req_info_2[-1]

            # Маскировка счета
            number_2_mask = f'**{number_2[-4:]}'

            # Добавление в список информации о платеже
            list_of_operations.append(f'{filter_date} {money_transfer}\n{"".join(req_info_2[:-1])} {number_2_mask}\n'
                                      f'{item["operationAmount"]["amount"]} '
                                      f'{item["operationAmount"]["currency"]["name"]}\n')

        else:
            req_info_1 = item['from'].split()
            number_1 = req_info_1[-1]

            # Маскировка счета
            number_1_mask = f'{number_1[0:4]} {number_1[4:6]}** **** {number_1[-4:]}'

            req_info_2 = item['to'].split()
            number_2 = req_info_2[-1]

            # Маскировка счета
            number_2_mask = f'**{number_2[-4:]}'

            # Добавление в список информации о платеже
            list_of_operations.append(f'{filter_date} {money_transfer}\n{"".join(req_info_1[:-1])} {number_1_mask} -> '
                                      f'{"".join(req_info_2[:-1])} {number_2_mask}\n'
                                      f'{item["operationAmount"]["amount"]} '
                                      f'{item["operationAmount"]["currency"]["name"]}\n')

    return '\n'.join(list_of_operations)
