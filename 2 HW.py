from fractions import Fraction
import random

# # Задача 1. Напишите программу, которая принимает на вход вещественное или
# целое число и показывает сумму его цифр. Через строку нельзя решать.
# # *Пример:*
# # - 6782 -> 23
# # - 0,56 -> 11

print('task1 - number_decision')
try:
    number = abs(Fraction(input('Enter a number: ')))
    while (number % 1 != 0):
        number *= 10
    sum_digit = 0
    int_number = int(number)
    while (int_number//1 > 0):
        sum_digit += int_number % 10
        int_number //= 10
    print(sum_digit)
except:
    print('Entered incorrect data')

print('task1 - string_decision')
try:
    sum_digit = 0
    str_number = (input('Enter a number: ')).replace(
        "-", "").replace(",", "").replace(".", "")
    for elem in str_number:
        sum_digit += int(elem)
    print(sum_digit)
except:
    print('Entered incorrect data')

# # Задача 2. Напишите программу, которая принимает на вход число N и выдает
# набор произведений чисел от 1 до N.
# # *Пример:*
# # - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

print('\ntask2')
try:
    number = float(input('Enter an integer positive number more zero: '))
    if number % 1 == 0 and number > 0:
        number = int(number)
        mult = 1
        arr_res = []
        for i in range(1, number+1):
            mult *= i
            arr_res.append(mult)
        print(arr_res)
    else:
        print('Entered incorrect data')
except:
    print('Entered incorrect data')

# # 3. Задайте список из n чисел последовательности (1+(1/n)^n и выведите
# на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

print('\ntask3')
try:
    number = float(input('Enter an integer positive number more zero: '))
    if number % 1 == 0 and number > 0:
        number = int(number)
        dict_pos = {}
        sum_val = 0
        for i in range(1, number + 1):
            dict_pos[i] = (1+(1/i))**i
            sum_val += dict_pos[i]
        print(dict_pos)
        print(sum_val)
    else:
        print('Entered incorrect data')
except:
    print('Entered incorrect data')

# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в
# файле file.txt в одной строке одно число.

print('\ntask4')
try:
    number = float(input('Enter an integer positive number more three: '))
    if number % 1 == 0 and number > 3:
        number = int(number)
        b = -1 * number
        arr_pos = []
        while b <= number:
            arr_pos.append(b)
            b += 1
        print(arr_pos)
        mult = 1
        with open('file.txt', 'r') as number_file:
            arr_str = number_file.read().split()
            for elem_pos in arr_str:
                mult *= arr_pos[int(elem_pos)]
        print(mult)
    else:
        print('Entered incorrect data')
except:
    print('Entered incorrect data')

# 5.Реализуйте алгоритм перемешивания списка.

print('\ntask5')
arr_pos = []
for i in range(10):
    arr_pos.append(i)
print(arr_pos)
for i in range(10):
    j = random.randint(0, 9)
    temp = arr_pos[i]
    arr_pos[i] = arr_pos[j]
    arr_pos[j] = temp
print(arr_pos)
