'''
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
'''

coins = [0]
eagles = 0
for i in coins:
    if i == 0:
        eagles += 1
tails = sum(coins) - eagles
if eagles <= tails:
    print("Number of coins to flip:", eagles)
else:
    print("Number of coins to flip:", tails)