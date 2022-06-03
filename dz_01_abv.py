"""Напишите программу, удаляющую из текста все слова содержащие "абв". Используйте знания с последней лекции.
Выполните ее в виде функции. """

def abv_filter(str_text):
    return ' '.join(filter(lambda s: 'абв' not in s, str_text.split()))

print(abv_filter(input('Введите строку для проверки: ')))