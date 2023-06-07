# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_1():
    """
    Тестовая функция. Проверяет деление единицы на себя. Маркирована как smoke
    :return: bool
    """
    assert all_division(1, 1) == 1


@pytest.mark.smoke
def test_11():
    """
    Тестовая функция. Проверяет деление числа на другое число. Маркирована как smoke
    :return: bool
    """
    assert all_division(2, 5) == 0.4


@pytest.mark.other
def test_100():
    """
    Тестовая функция. Проверяет деление 100 на число. Маркирована как other
    :return: bool
    """
    assert all_division(100, 2) == 50.0


@pytest.mark.other
def test_minus():
    """
    Тестовая функция. Проверяет деление числа на отрицательное число. Маркирована как other
    :return: bool
    """
    assert all_division(2, -2) == -1.0


@pytest.mark.zero
def test_zero():
    """
    Тестовая функция. Проверяет деление на ноль. Маркирована как zero
    :return: bool
    """
    with pytest.raises(ZeroDivisionError):
        all_division(2, 0)
