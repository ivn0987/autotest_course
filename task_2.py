# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчнию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# func2()
# func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47

# Со звёздочкой. ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО.
# help(func1) должен выводит одинаковый текст, когда есть декоратор на функции func1 и когда его нет
# Реализовать без подключения новых модулей и сторонних библиотек.


import datetime


def func_log(file_log='log.txt'):
    """
    Декоратор для логирования
    :param file_log: str Путь до файла с логами, по умолчанию log.txt
    :return: Обертка wrapper_2
    """
    def wrapper_2(func):
        """
        Функция-обертка верхнего уровня. Принимает декорируемую функцию, возвращает вложенную обертку
        :param func: Декорируемая функция
        :return: Обертка wrapper
        """
        def wrapper():
            """
            Функция-обертка.
            Записывает в переданный файл имя переданной функции
            и время вызова в формате имя_функции вызвана %d.%m %H:%M:%S
            """
            call_time = datetime.datetime.now().strftime('%d.%m %H:%M:%S')
            func_name = func.__name__
            func()
            with open(file_log, 'a', encoding='utf-8') as file:
                file.write(f'{func_name} вызвана {call_time} \n')
        wrapper.__doc__ = func.__doc__  # А это решение задачи со звездочкой
        return wrapper
    return wrapper_2
