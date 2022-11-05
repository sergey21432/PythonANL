from decimal import Decimal
import random

# Задача 1. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

print('task1')


def calc_pi(val_accuracy):
    try:
        numb_accuracy = len(str("{0:f}".format(val_accuracy))) - 1
        NUMB = 4
        sum_calc_pi = 0
        counter = 0
        while True:
            val_fraction = Decimal(NUMB / (1 + 2 * counter))
            if counter % 2 != 0:
                val_fraction *= -1
            sum_calc_pi += val_fraction
            if val_fraction * (10 ** numb_accuracy) // 1 == 0:
                break
            else:
                counter += 1
        return round(sum_calc_pi, numb_accuracy - 1)
    except:
        return 'Error'


def get_accuracy():
    try:
        val_accuracy = Decimal(input('Enter the accuracy like pattern "0.001": '))
        if (val_accuracy < 0 or val_accuracy == 0 or int(val_accuracy) != 0 or
            len(str(val_accuracy)) > 12):
            return None
        else:
            return val_accuracy
    except:
        return None


while True:
    accuracy = get_accuracy()
    if not (accuracy is None):
        break
    print('Entered incorrect data. Retry again.')
print(calc_pi(accuracy))

# Задача 2. Задайте натуральное число N. Напишите программу, которая составит
# список простых множителей числа N.

print('\ntask2')


def get_natural_number():
    try:
        str_message = 'Enter the natural number more zero: '
        number = float(input(str_message))
        if number % 1 == 0 and number > 0:
            return int(number)
        else:
            return None
    except:
        return None


def get_list_prime_factors(number_val):
    lst_prime_factors = []
    min_number = 2
    while number_val != 1:
        if len(lst_prime_factors) > 0:
            min_number = max(lst_prime_factors)
        for i in range(min_number, number_val + 1):
            if number_val % i == 0:
                if not (i in lst_prime_factors):
                    lst_prime_factors.append(i)
                while(number_val % i == 0):
                    number_val //= i
                break
    return lst_prime_factors


while True:
    number = get_natural_number()
    if not (number is None):
        break
    print('Entered incorrect data. Retry again.')
print(get_list_prime_factors(number))

# Задача 3. Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности.

print('\ntask3')


def get_uniq(arr_int):
    try:
        arr_uniq = arr_int.copy()
        arr_uniq.sort()
        for i in range(len(arr_int)):
            while arr_uniq[i] == arr_uniq[i + 1]:
                del arr_uniq[i + 1]
        return arr_uniq
    except:
        return arr_uniq


def get_notRepeat(arr_int):
    try:
        arr_res = []
        arr_temp = arr_int.copy()
        arr_temp.sort()
        for i in range(len(arr_temp)):
            if arr_temp.count(arr_temp[i]) == 1:
                arr_res.append(arr_temp[i])
        return arr_res
    except:
        return arr_res


lst = []
for i in range(13):
    lst.append(random.randint(1, 10))
print(lst)
print(get_uniq(lst))
print(get_notRepeat(lst))

# Задача 4. Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена и записать в файл
# многочлен степени k.
# Пример:- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

print('\ntask4')


def get_power():
    try:
        str_message = 'Enter the power of number: '
        number = float(input(str_message))
        if number % 1 == 0 and number > -1:
            return int(number)
        else:
            return None
    except:
        return None


def get_string_polynom(numb_val):
    try:
        str_polynom = ''
        for i in range(numb_val + 1):
            int_coef = random.randint(0, 100)
            if int_coef != 0:
                str_member = ''
                if i != 0:
                    str_member += '+'
                if int_coef != 1 or i == numb_val:
                    str_member += f'{int_coef}' 
                if i != numb_val:
                    if int_coef != 1:
                        str_member += '*'
                    str_member += f'x^{numb_val - i}'
                str_polynom += str_member
        return str_polynom
    except:
        return 'Error'


while True:
    power_numb = get_power()
    if not (power_numb is None):
        break
    print('Entered incorrect data. Retry again.')
with open('file.txt', 'w') as number_file:
    number_file.write(get_string_polynom(power_numb))
number_file.close()

# Задача 5.  Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

print('\ntask5')
# не успел, доделаю

# def get_sum_polynom(str_polyn_1, str_polyn_2):
#     try:
#         str_sum_polynom = ''
#         ToDo: цикл на постепенной поиск и суммирование коэффициентов,
#           может словарь?
#         return str_sum_polynom
#     except:
#         return 'Error'


def read_file(number):
    with open(f'file_{number}.txt', 'r') as number_file:
        str_polynom = number_file.read()
    number_file.close()
    return str_polynom


lst_polyn = []
for i in range(1, 3):
    lst_polyn.append(read_file(i))
