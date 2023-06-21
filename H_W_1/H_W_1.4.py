'''Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
*Пример:*
3 2 4 -> yes
3 2 1 -> no'''

length_choc = int(input('Введите количество долек по горизонтали: '))
width_choc = int(input('Введите количество долек по вертикали: '))
number_of_slices = int(input('Введите количество долек, которые хотите отломать: '))
if number_of_slices % length_choc == 0 or  number_of_slices % width_choc == 0:
    print (length_choc, width_choc, number_of_slices, '-> yes')
else:
     print (length_choc, width_choc, number_of_slices, '-> no')
