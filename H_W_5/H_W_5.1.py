# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

a = int(input('Укажите число A: '))
b = int(input('Укажите число B: '))

def exponentiation(A, B):
    if B == 0:
        return 1
    elif B < 0:
        return 1 / exponentiation(A, -B)
    else:
        return A * exponentiation(A, B - 1)

print(f"A = {a}; B = {b} -> {exponentiation(a, b)}")