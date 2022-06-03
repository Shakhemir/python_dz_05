"""Чисто для тренировки новый функций, ничего сложного. Создайте два списка — один с названиями языков
программирования, другой — с числами от 1 до длины первого плюс 1. Вам нужно сделать две функции: первая из которых
создаст список кортежей, состоящих из номера и языка, написанного большими буквами. Вторая — которая отфильтрует этот
список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже,
то кортеж остается, его номер заменяется на сумму очков. Если нет — удаляется. Суммой очков называется сложение
порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем столбце:
https://www.charset.org/utf-8 Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы. С
помощью reduce сложите получившиеся числа и верните из функции в качестве ответа. """

from functools import reduce

langs = ["Basic", "Pascal", "Assembler", "C++", "Java", "C#", "Swift", "Kotlin", "Python", "Go", "JavaScript"]
numbers = [i for i in range(1, len(langs) + 1)]


def tuple_list():
    return tuple(zip(numbers, [lang.upper() for lang in langs]))


def filter_list(in_tuple):
    out_list = []
    for index, name in in_tuple:
        summa_ochkov = reduce(lambda x, y: x + ord(y) - ord('A') + 1, name, 0)
        delitel_list = [i for i in range(1, summa_ochkov // 2 + 1) if not summa_ochkov % i]
        if index in delitel_list:
            out_list.append((summa_ochkov, name))
    return tuple(out_list)


langs_tuple = tuple_list()
print(langs_tuple)
langs_tuple_filtered = filter_list(langs_tuple)
print(langs_tuple_filtered)
