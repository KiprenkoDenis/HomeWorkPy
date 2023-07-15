# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def arith_prog_array():
    first_elem = int(input('Укажите первый элемент прогрессии: '))
    diff_prog = int(input('Укажите разность прогрессии: '))
    size_prog = int(input('Укажите количество элементов прогрессии: '))

    array_prog = []
    coef_prog = 1
    array_prog.append(first_elem)
    for i in range(1, size_prog):
        n = first_elem + diff_prog * coef_prog
        coef_prog += 1
        array_prog.append(n)
    return(array_prog)

<<<<<<< HEAD
print(arith_prog_array())
=======
print(arith_prog_array())
>>>>>>> 76b1cd6f7a4383c2bdb6b4e017ec80f6d4b0af9b
