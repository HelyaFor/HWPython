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


def input_data(a=None):
    name = write_name()
    surname = write_surname()
    phone = write_phone()
    adress = write_adress()
    with open('phonebook.txt', 'a', encoding='utf-8') as data:
        data.write(f'{name} {surname}: {phone}\n{adress}\n\n')


def print_data():
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        data_first = data.readlines()
        for line in data_first:
            print(line, end='')


def search_line():
    search = input('Введите данные для поиска: ')
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        temp = data.readlines()
        data_first = ''.join(temp).split('\n\n')
        for line in data_first:
            if search in line:
                print(line)

# def edit_line(new_name, former_name):
#     contacts = search_line()
#     former_name = input('Введите, кого хотите переименовать: ')
#     new_name = input ('Введите новые данные: ')
#     with open('phonebook.txt', 'r', encoding='utf-8') as data:
#         for contact in contacts:
#             if former_name != contact:
#                 data.write(contact)
#             else:
#                 data.write(new_name + '\n')
    
# def deleted_data():
#     contacts = search_line()
#     with open('phonebook.txt', 'r', encoding='utf-8') as data:
#         name = input('Введите, кого хотите удалить: ')
#         for contact in contacts:
#             if name != contact:
#                 data.write(contact)

def edit_line():
    former_name = input('Введите, кого хотите переименовать: ')
    new_name = input('Введите новые данные: ')
    
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        contacts = data.readlines()
    
    with open('phonebook_temp.txt', 'w', encoding='utf-8') as temp_data:
        for contact in contacts:
            if former_name in contact:
                temp_data.write(new_name + '\n')
            else:
                temp_data.write(contact)
    
    os.remove('phonebook.txt')
    os.rename('phonebook_temp.txt', 'phonebook.txt')
    
def deleted_data():
    name = input('Введите, кого хотите удалить: ')
    
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        contacts = data.readlines()
    
    with open('phonebook_temp.txt', 'w', encoding='utf-8') as temp_data:
        for contact in contacts:
            if name not in contact:
                temp_data.write(contact)
    
    os.remove('phonebook.txt')
    os.rename('phonebook_temp.txt', 'phonebook.txt')