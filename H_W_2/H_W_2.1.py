'''На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть'''

number_of_coins = int(input('Укажите количество монет: '))
inside_coins = int(input('Укажите сколько из них лежат вверх решкой: '))
outside_coins = number_of_coins - inside_coins
flip_result = 0
for i in range(number_of_coins):
    if inside_coins < outside_coins:
        flip_result = inside_coins
    elif inside_coins >= outside_coins:
        flip_result = outside_coins
print('минимальное количество монет, которые нужно перевернуть: {}'.format(flip_result))
