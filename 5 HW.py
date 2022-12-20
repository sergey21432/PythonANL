from decimal import Decimal
import random

# Задача 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

print('\ntask1')


def get_clear_text(strText):
    checkStr = 'абв'
    lstResult = [x for x in strText.split() if checkStr not in x]
    return lstResult


def get_text(strPreInput):
    try:
        return input(strPreInput)
    except:
        return None


while True:
    strText = get_text('Enter the text: ')
    if not (strText is None):
        break
    print('Entered incorrect data. Retry again.')
print(" ".join(get_clear_text(strText)))

# Задача 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход
# друг после друга. Первый ход определяется жеребьёвкой. За один ход можно
# забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему
# последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все
# конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

print('\ntask2')


def get_name_player(numberPlayer):
    while True:
        strName = get_text(f'Player {numberPlayer}, please, enter your name: ')
        if not (strName is None) and strName != 'IvanAI' and strName != 'invincibleAI':
            return strName
        print('Entered incorrect data. Retry again.')


def get_number_candie(strPreInput, intMax):
    try:
        number = float(input(strPreInput))
        if number % 1 == 0 and number >= 0 and number <= intMax:
            return int(number)
        else:
            return None
    except:
        return None


def get_number(strPreInput, intMax):
    try:
        number = float(input(strPreInput))
        if number % 1 == 0 and number > 0 and number <= intMax:
            return int(number)
        else:
            return None
    except:
        return None


def do_step(strName, totalCandie, intMod):
    INT_MAX = 28
    if totalCandie < INT_MAX: numberCandieForStep = totalCandie
    else: numberCandieForStep = INT_MAX

    if intMod == 1 and strName == 'IvanAI':
        intCandie = random.randint(1, numberCandieForStep)
        print(f'{strName} takes {intCandie} candies.')
        return intCandie
    elif intMod == 3 and strName == 'invincibleAI':
        if totalCandie <= INT_MAX: intCandie = totalCandie
        else: intCandie = (totalCandie - (INT_MAX + 1)) % INT_MAX
        print(f'{strName} takes {intCandie} candies.')
        return intCandie
    else:
        while True:
            intCandie = get_number_candie(f'{strName}, your move, take a candie, enter a number no more then {numberCandieForStep}: ', numberCandieForStep)
            if not (intCandie is None):
                return intCandie


def introduce_game(strPreInput):
    while True:
        intMod = get_number(strPreInput, 3)
        if not (intMod is None):
            return intMod


strPreInput = 'Welcome, enter "1" like number to play with AI or enter "2" like number to play with two players. Also if you want to play with invincible AI enter "3" like number: '
intMod = introduce_game(strPreInput)
strNameFirst = get_name_player(1)
if intMod == 2: strNameSecond = get_name_player(2)
elif intMod == 1: strNameSecond = 'IvanAI'
elif intMod == 3: strNameSecond = 'invincibleAI'
totalCandie = 100
switchPlayer = random.randint(0, 1)
while totalCandie > 0:
    if switchPlayer: strName = strNameFirst
    else: strName = strNameSecond
    totalCandie -= do_step(strName, totalCandie, intMod)
    print(f'There are {totalCandie} candies left.')
    switchPlayer = not switchPlayer
else:
    if not switchPlayer: strName = strNameFirst
    else: strName = strNameSecond
    strNameWinner = strName
    if strNameWinner == 'IvanAI' or strNameWinner == 'invincibleAI': print(f'Unfortunately, you lost. Retry again to win.')
    else: print(f'Greetings, {strNameWinner}, you are win.')


# Задача 3. Создайте программу для игры в ""Крестики-нолики"".

print('\ntask3')


def do_step_XO(strName, strSymbol, lstPaper):
    print(f'{strName}, your move.')
    while True:
        while True:
            intRow = get_number('Enter number row of position to paint from 1 to 3: ', 3)
            if intRow is None: print('Incorrect number, retry again.')
            else:
                intRow -= 1
                break
        while True:
            intCol = get_number('Enter number column of position to paint from 1 to 3: ', 3)
            if intCol is None: print('Incorrect number, retry again.')
            else: 
                intCol -= 1
                break
        if lstPaper[intRow][intCol] == '-':
            oldStr = lstPaper[intRow]
            newStr = oldStr[:intCol] + strSymbol + oldStr[intCol+1:]
            lstPaper[intRow] = newStr
            return lstPaper
        else: print("It's painted. Please, select another position.")


def check_Win(lstPaper, strSymbol):
    lstEmptyRow = []
    for i in range(3):
        intCountRow = lstPaper[i].count(strSymbol)
        if intCountRow == 0: lstEmptyRow.append(i)
        elif intCountRow == 3: return True
    if len(lstEmptyRow) == 0:
        for i in range(3):
            if lstPaper[0][i] == strSymbol:
                intCountCol = 1
                for j in range(2):
                    if lstPaper[j][i] != lstPaper[j + 1][i]: break
                    else: intCountCol += 1
                if intCountCol == 3: return True
                elif i == 0 or i == 2:
                    intCountCol = 0
                    for j in range(3):
                        if lstPaper[j][abs(i - j)] == strSymbol: intCountCol += 1
                        else: break
                    if intCountCol == 3: return True
    return False


def check_Continue(lstPaper):
    for i in range(3):
        if lstPaper[i].count('-') > 0: return True
    return False


def print_XO(lstPaper):
    for elem in lstPaper:
        print(elem)


strNameFirst = get_name_player(1)
strNameSecond = get_name_player(2)
lstPaper = ['-' * 3 for _ in range(3)]
print_XO(lstPaper)
switchPlayer = random.randint(0, 1)
blnContinue = True
while True:
    if switchPlayer:
        strName = strNameFirst
        strSymbol = 'X'
    else:
        strName = strNameSecond
        strSymbol = 'O'
    lstPaper = do_step_XO(strName, strSymbol, lstPaper)
    print_XO(lstPaper)
    if check_Win(lstPaper, strSymbol):
        print(f'Greetings, {strName}, you are win.')
        break
    elif not check_Continue(lstPaper):
        print('All positions are painted, not winners.')
        break
    switchPlayer = not switchPlayer


# Задача 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления
# данных.

print('\ntask4')


def do_compress(strText):
    intCount = 1
    lstResult = []
    for i in range(len(strText)):
        try:
            if strText[i + 1] == strText[i]:
                intCount += 1
            else:
                lstResult.append((intCount, strText[i]))
                intCount = 1
        except:
            lstResult.append((intCount, strText[i]))
    return lstResult


def do_rebuild(lstLRE):
    text = ''
    for ctg in lstLRE:
        text += ctg[1] * ctg[0]
    return text


text = 'fff ggggyy ykkkvv vll'
lstCompress = do_compress(text)
print(lstCompress)
print (do_rebuild(lstCompress))
