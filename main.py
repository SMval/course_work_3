from utils import get_operations, sort_operations_by_date, get_five_executed, get_data

# Получение списков словарей из файла и их преобразование
transformation_json = get_operations()

# Сортировка списка словарей по дате
sort_by_date = sort_operations_by_date(transformation_json)

# Получение 5 последних выполненных операций
five_executed = get_five_executed(sort_by_date)

# Получение окончательного варианта в нужном формате
list_4 = get_data(five_executed)

# Вывод 5 последних выполненных клиентом операций
print(list_4)
