from utils import get_operations, sort_operations_by_date, get_five_executed, get_data

list_1 = get_operations()
list_2 = sort_operations_by_date(list_1)
list_3 = get_five_executed(list_2)
list_4 = get_data(list_3)

print(list_4)