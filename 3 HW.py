from decimal import Decimal
import random

# # Задача 1. Задайте список из нескольких чисел. Напишите программу, которая
# найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

print('task1')


def CheckInt(number):
    try:
        number = float(number)
        if number % 1 == 0 and number > 0:
            return True
        else:
            return False
    except:
        return False


def IntArr(number_val, int_arr):
    int_arr = []
    sum = 0
    for i in range(number_val):
        n = random.randint(1, 1000)
        int_arr.append(n)
        if i % 2 != 0:
            sum += n
    print(int_arr)
    print(f'Sum odd elements: {sum}')
    return int_arr


val_arr = []
while len(val_arr) == 0:
    number = input('Enter an integer positive number more zero: ')
    if CheckInt(number):
        number = int(number)
        val_arr = IntArr(number, val_arr)
    else:
        print('Entered incorrect data')

# Задача 2.  Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

print('\ntask2')


def Mult_Couple(int_arr):
    len_arr = len(int_arr)
    if not (len_arr > 0):
        return None
    arr_mult = []
    for i in range((len_arr + 1) // 2):
        arr_mult.append(int_arr[i] * int_arr[len_arr - (i + 1)])
    return arr_mult


print(Mult_Couple(val_arr))

# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая
# найдёт разницу между максимальным и минимальным значением дробной части
# элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

print('\ntask3')

lst = [11]


def Dif_Frac_Arr(fl_arr):
    len_arr = len(fl_arr)
    if not (len_arr > 0):
        return None
    bln_first = True
    len_max_string = 0
    for i in range(len_arr):
        str_fl = str(fl_arr[i])
        try:
            len_string = len(str_fl[str_fl.index('.') + 1:])
            if len_max_string < len_string:
                len_max_string = len_string
        except: 
            len_string = 0
        finally:
            temp_fl = Decimal(fl_arr[i]) - int(fl_arr[i])
            if temp_fl != 0:
                if not bln_first:
                    if temp_fl > max_Frac:
                        max_Frac = temp_fl
                    if temp_fl < min_Frac:
                        min_Frac = temp_fl
                if bln_first:
                    max_Frac = temp_fl
                    min_Frac = temp_fl
                    bln_first = False
    try:
        return round(max_Frac - min_Frac, len_max_string)
    except:
        return None


print(Dif_Frac_Arr(lst))

# Задача 4. Напишите программу, которая будет преобразовывать десятичное 
# число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

print('\ntask4')


def Convert_Bin(number_val):
    bin_numb = 0
    count = 0
    while number_val > 0:
        bin_numb += number_val % 2 * (10 ** count)
        number_val //= 2
        count += 1
    return bin_numb


number = input('Enter an integer positive number more zero: ')
if CheckInt(number):
    number = int(number)
    print(Convert_Bin(number))
else:
    print('Entered incorrect data')


# # Задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для
# # отрицательных индексов.
# # Пример: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

print('\ntask5')


def Arr_Neg_Fib(number_val):
    arr_fib = []
    if number_val >= 1:
        arr_fib.append(0)
    if number_val >= 2:
        arr_fib.append(1)
        arr_fib.insert(0, 1)
    if number_val >= 3:
        for i in range(2, number_val):
            temp_numb = arr_fib[i] + arr_fib[i - 1]
            arr_fib.append(temp_numb)
        indx_cur = len(arr_fib) - 1
        if number_val % 2 == 0: int_corr = 1
        else: int_corr = -1           
        for i in range(2, number_val):
            arr_fib.insert(i - 2, arr_fib[indx_cur] * int_corr)
            int_corr *= -1
    return arr_fib


print(Arr_Neg_Fib(number))
