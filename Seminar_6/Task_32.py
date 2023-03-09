'''Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)'''
#         0  1  2  3   4   5  6  7   8  9   10 11 12  13 14  15  16 17  18  19
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]   9, 10, 8, 10, 7

lst = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
n_max = int(input("Введите максимальное число -> "))
n_min = int(input("Введите минимальное число -> "))
for i in range(len(lst)):
    if lst[i] < n_max and lst[i] > n_min:
        print(i)