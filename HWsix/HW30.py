# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input("Enter the first element of the arithmetic progression: ")) 
d = int(input("Enter the progression difference: "))
n = int(input("Enter the number of progression elements: "))
array = []
for i in range(0, n):
    array.append(a1)
    a1 += d
print("The resulting array:", array)


