"""
Единичная дробь имеет 1 в числителе. Десятичные представления единичных дробей со знаменателями от 2 до 10 даны ниже:

1/2=0.5 1/3=0.(3) 1/4=0.25 1/5=0.2 1/6=0.1(6) 1/7=0.(142857) 1/8=0.125 1/9=0.(1) 1/10=0.1 Где 0.1(6) значит
0.166666..., и имеет повторяющуюся последовательность из одной цифры. Заметим, что 1/7 имеет повторяющуюся
последовательность из 6 цифр.

Найдите значение d < 1000, для которого 1/d в десятичном виде содержит самую длинную повторяющуюся последовательность
цифр.
"""
from decimal import *
from tqdm import tqdm


def repeats(string):
    """
    Эту функцию нашел в интернете и немного модифицировал.
    Изначально она обнаруживала повторяемость в тексте,
    например repeats('pythonpytho') возвращала 'python'
    Т.е. если повторяемость "обрубалась" в конце, то она это учитывала.
    Мне пришлось немного модифицировать, т.к. если в дроби в конце только один символ повторился с первым,
    то функция считала, что этого достаточно чтоб посчитать весь кусок повторяющимся
    """
    for x in range(1, len(string)):
        substring = string[:x]
        string_mod = substring[:len(string) % len(substring)]
        if substring * (len(string) // len(substring)) + string_mod == string:  # проверка на поторяемость текста
            if len(string_mod) * 2 > len(substring):  # остаток не должен быть слишком маленьким
                return substring
    return False

def check_fraction_repeat(fract):
    fract = str(fract).split('.')[1][:-1]  # последний символ часто "портил" статистику
    # так как повторяемость могла начаться не сразу, то пропускаем первые 10 символов в цикле
    for i in range(10):
        repeat_part = repeats(fract[i:])
        if repeat_part:
            return repeat_part
    return False


digits = 60000  # количество возможных символов после точки
getcontext().prec = digits  # задаем насколько длинная десятичная дробь
"""
Пришлось задать большое значение этой переменной, т.к. от нее сильно зависел результат
и он был разным по мере увеличения этого значения 
"""
max_repeat = ''
max_denominator = 1

for i in tqdm(range(2, 1000)):
    fract = Decimal(1)/Decimal(i)
    rep_part = check_fraction_repeat(fract)  # проверяем на повторяемость символов
    if rep_part:
        if len(rep_part) > len(max_repeat):
            max_repeat = rep_part
            max_denominator = i

print(f'Дробь: 1/{max_denominator}\n={Decimal(1)/Decimal(max_denominator)}')
print(f'Самая длинная повторяющаяся последовательность цифр:\n{max_repeat}')
print(f'Длина повторяющейся части: {len(max_repeat)} из {digits}')