

def remove_value(_list, target):
    return [i for i in _list if target != i]
    src_list = _list[:]
    while target in src_list:
        src_list.remove(target)
    retrun src_list


numbers = [1, 2, 3, 2, 4, 2, 5]
value_remove = 2
new_numbers = remove_value(numbers, value_remove)
print(numbers, new_numbers)