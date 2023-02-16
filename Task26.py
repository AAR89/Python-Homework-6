# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint
list = [randint (1, 10) for i in range(0, 10)]
print(list)
min = int(input('Введите минимум: '))
max = int(input('Введите максимум: '))
for i in range(len(list)):
    if min <= list[i] <= max:
        print(i, end = " ")