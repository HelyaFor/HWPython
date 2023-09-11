# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)


array = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min = int(input("Enter the minimum element of the range: "))
max = int(input("Enter the maximum element of the range: "))
for i in range(len(array)):
    if (array[i] >= min) and (array[i] <= max):
        print(i)
