import pytest
import time


@pytest.fixture()
def end_time():
    """
    Фикстура для конкретного теста, возвращающая текущее время
    :return: float Время
    """
    return time.time()


@pytest.fixture(scope='class')
def class_end_time():
    """
    Фикстура для класса, возвращает время окончания класса и длительность тестов
    :return: float Время
    """
    start = time.time()
    yield print(f'Начало выполнения класса: {time.time()}')
    end = time.time()
    return print(f'Окончание выполнения класса: {end}\nДлительность тестов: {end - start}')
