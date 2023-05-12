# Напишите функцию sum_digits, которая принимает положительное число num,
# и возвращает сумму цифр our_sum.
# Например (Ввод --> Вывод) :
#
# 39 --> 12
# 999 --> 27
# 4 --> 4

def sum_digits(num):
    """
    Функция принимает положительное число num и возвращает его сумму цифр our_sum
    :param num: int Положительное целое число
    :return: (our_sum) int Сумма цифр num
    """
    our_sum = 0
    str_num = str(num)
    index = 0
    while index < len(str_num):
        our_sum += int(str_num[index])
        index += 1
    return our_sum

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    39, 4, 25, 999, 5050, 222333444
]

test_data = [
    12, 4, 7, 27, 10, 27
]


for i, d in enumerate(data):
    assert sum_digits(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
