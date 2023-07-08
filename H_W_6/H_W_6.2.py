#  Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

def index_determinant(orig_list, min_elem, max_elem):
    new_list = []
    for i in range(len(orig_list)):
        if  min_elem <= orig_list[i] <= max_elem:
            new_list.append(i)
    return(new_list)

list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_num = 7
max_num = 10
print(index_determinant(list_1, min_num, max_num))

