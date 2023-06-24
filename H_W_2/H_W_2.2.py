'''
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.
'''

summa = int(input("Введите сумму чисел: "))
product = int(input("Введите произведение чисел: "))

found_numbers = False
for first_number in range(1, summa+1):
    if product % first_number == 0:
        second_number = product // first_number
        if first_number + second_number == summa:
            print("Отгаданные числа: ", first_number, "и", second_number)
            found_numbers = True

if not found_numbers:
    print("Нет чисел удовлетворяющим условию") 