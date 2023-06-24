'''Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.'''

number_n = int(input('Укажите число N: '))
k = 0
power_of_two = 1
while power_of_two <= number_n:
    print(power_of_two)
    k += 1  
    power_of_two = 2 ** k 
    