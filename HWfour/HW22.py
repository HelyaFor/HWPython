# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random
n = int(input("Enter the value of N: "))
set_n = random.sample(range(20), n)
print(set_n)
m = int(input("Enter the value of M: "))
set_m = random.sample(range(20), m)
print(set_m)
print(set(set_n) | set(set_m))
print(sorted(set(set_n).intersection(set(set_m))))



