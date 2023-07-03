# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

array_size = int(input('Укажите количество элементов массива: '))
my_list_1 = list()
for i in range(array_size):
    n = int(input('Введите элемент массива: '))
    my_list_1.append(n)
    print( my_list_1)


number_x = int(input('Укажите число X: '))
nearest_element = None
min_difference = float('inf')

for i in my_list_1:
    difference = abs(number_x - i)
    if difference < min_difference:
        min_difference = difference
        nearest_element = i
print(f"-> {nearest_element}")




