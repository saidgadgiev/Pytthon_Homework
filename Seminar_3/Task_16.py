'''Задача 16: Требуется вычислить, сколько раз встречается некоторое 
число X в массиве A[1..N]. Пользователь в первой строке вводит 
натуральное число N – количество элементов в массиве. В последующих  
строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1'''
#__________________________________________________
print ("-------------")    
print ("Вариант решения 1")
# n_ = 5 
n_list = [1, 3, 2, 3, 5, 3, 3, 9, 2]
a = 3
count=0
for i in n_list:
    if a == i:
        count +=1
print ("В списке чисел -> ", n_list )
print(f"Число {a} встречаеться  {count} ")

#_____________________________________________________

print ("-------------")
print ("Вариант решения 2")
print()

import random
n = 10
list = [random.randrange(10) for _ in range(n)]
x = int(input("Введите число X от 1 до 10-> "))
count=0
for i in list:
    if x == i:
        count +=1

print("Количесво элементов в массиве -> ", n) # Количесво элементов в массиве рандомно
print ("Cозданный список - > ", list) # Вывод созданного списка рандомно

print(f"Число {x} встречаеться  {count} ")

#_________________________________________________________