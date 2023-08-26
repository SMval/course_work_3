from utils import sort_operations_by_date, get_five_executed, get_data

dict_1 = [
    {
        'date': "2019-08-26T10:50:58.294041"
    },
    {
        'date': "2020-08-26T10:50:58.294041"
    },
    {

    }
]

dict_2 = [
    {
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041"
    },
    {"state": "EXECUTED",
     "date": "2018-08-26T10:50:58.294041"},
    {"state": "EXECUTED",
     "date": "2017-08-26T10:50:58.294041"},
    {"state": "EXECUTED",
     "date": "2016-08-26T10:50:58.294041"},
    {"state": "EXECUTED",
     "date": "2015-08-26T10:50:58.294041"},
    {"state": "EXECUTED",
     "date": "2014-08-26T10:50:58.294041"},
    {"state": "EXECUTED",
     "date": "2013-08-26T10:50:58.294041"}
]

dict_3 = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }
]


def test_sort_operations_by_date():
    assert sort_operations_by_date(dict_1) == [{'date': '2020-08-26T10:50:58.294041'},
                                               {'date': '2019-08-26T10:50:58.294041'}, {}]


def test_get_five_executed():
    assert get_five_executed(dict_2) == [{'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041'},
                                         {'state': 'EXECUTED', 'date': '2018-08-26T10:50:58.294041'},
                                         {'state': 'EXECUTED', 'date': '2017-08-26T10:50:58.294041'},
                                         {'state': 'EXECUTED', 'date': '2016-08-26T10:50:58.294041'},
                                         {'state': 'EXECUTED', 'date': '2015-08-26T10:50:58.294041'}]


def test_get_data():
    assert get_data(dict_3) == (f'26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n'
                                f'31957.58 руб.\n')
