#  Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1


array_size = int(input('Укажите количество элементов массива: '))
my_list = list()
for i in range(array_size):
    n = int(input('Введите элемент массива: '))
    my_list.append(n)
    print( my_list)
number_x = int(input('Укажите число X: '))
number_x_count = my_list.count(number_x)
print(f"-> {number_x_count}")