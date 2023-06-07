# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string


def generate_random_name():
    """
    Функция возвращает два слова из латинских букв длиной от 1 до 15 символов, разделенных пробелом
    :return: str Два слова из латинских букв, разделенных пробелом, длиной от 1 до 15 символов
    """
    first_world = ''
    second_world = ''
    while True:
        how_many_symbols_first = random.randrange(1, 16)
        how_many_symbols_second = random.randrange(1, 16)
        for item in range(how_many_symbols_first):
            random_symbol = random.choice(string.ascii_lowercase)
            first_world += random_symbol
        for item in range(how_many_symbols_second):
            random_symbol = random.choice(string.ascii_lowercase)
            second_world += random_symbol
        yield f'{first_world} {second_world}'
        first_world = ''
        second_world = ''
