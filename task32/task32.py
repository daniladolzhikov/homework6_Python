# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума). 
# Список можно задавать рандомно
# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

def find_indices_in_range(arr, min_val, max_val):
    indices = []

    for i, val in enumerate(arr):
        if min_val <= val <= max_val:
            indices.append(i)

    return indices

input_list = list(map(int, input("Введите элементы списка через пробел: ").split()))
min_range = int(input("Введите минимум диапазона: "))
max_range = int(input("Введите максимум диапазона: "))

result = find_indices_in_range(input_list, min_range, max_range)
print("Индексы элементов в заданном диапазоне:", result)