# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы

a = int(input('Укажите число a: '))
b = int(input('Укажите число b: '))

def sum_pos_int(a, b):
    if a == 0:  
        return b
    elif b == 0:  
        return a
    else:
        return sum_pos_int(a - 1, b + 1)

result = sum_pos_int(a, b)
print(result)
