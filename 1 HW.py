# задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет

import random
print('task_1')
try:
    a = input('Enter a number day of week: ')
    if (float(a) % 1 != 0 or int(a) < 1 or int(a) > 7):
        print('Entered incorrect data')
    elif (int(a) > 5):
        print("It's a weekend")
    else:
        print("It's a weekday")
except:
    print('Entered incorrect data')

# задача 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print('\ntask_2')
try:
    a = [True, False]
    for x in a:
        for y in a:
            for z in a:
                print(
                    f'x: {x}, y: {y}, z: {z}, ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z: {not (x or y or z) == (not x and not y and not z)}')
except:
    print('Entered incorrect data')

# задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y), и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print('\ntask_3')
try:
    x = float(input('Enter a value X: '))
    y = float(input('Enter a value Y: '))
    if (x == 0):
        print("X")
    elif (y == 0):
        print("Y")
    elif (x == 0 and y == 0):
        print("0")
    elif (y > 0):
        if (x > 0):
            print("1")
        elif (x < 0):
            print("2")
    elif (y < 0):
        if (x > 0):
            print("4")
        elif (x < 0):
            print("3")
except:
    print('Entered incorrect data')


# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

print('\ntask_4')
try:
    a = int(input('Введите номер координатной плоскости от 1 до 4: '))
    if a == 1:
        print('x>0, y>0')
    elif a == 2:
        print('x<0, y>0')
    elif a == 3:
        print('x<0, y<0')
    elif a == 4:
        print('x>0, y<0')
    else:
        print('Введены некорректные данные')
except:
    print('Введены некорректные данные')

# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# *Пример:*
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print('\ntask5')
try:
    x1 = float(input('Enter X coordinate for point I: '))
    y1 = float(input('Enter Y coordinate for point I: '))
    x2 = float(input('Enter X coordinate for point II: '))
    y2 = float(input('Enter Y coordinate for point II: '))

    result = round(((x2 - x1)**2 + (y2-y1)**2)**0.5, 2)

    print(result)

except:
    print('Введены некорректные данные')
