# Напишите функцию multiplication_chain, которая принимает положительное число num,
# и возвращает количество раз count_multy, которое вы должны перемножить цифры числа num и полученных произведений,
# пока не получите одну цифру.
# Например (Ввод --> Вывод) :
#
# 39 --> 3 (потому что 3*9 = 27, 2*7 = 14, 1*4 = 4, вот 4 одна цифра. Итого 3 итерации)
# 999 --> 4 (потому что 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, наконец 1*2 = 2, Итого 4 итерации)
# 4 --> 0 (4 уже одна цифра, а значит мы проделали 0 итераций)

def multiplication_chain(num):
    """
    Функция принимает положительное число num и возвращает количество операций перемножения цифр count_multy
    :param num: int Положительное число
    :return: (count_multy) int Число операций перемножения цифр числа num
    """
    count_multy = 0
    str_num = str(num)
    while len(str_num) > 1:
        product_of_numbers = 1
        for number in str_num:
            product_of_numbers *= int(number)
        str_num = str(product_of_numbers)
        count_multy += 1
    return count_multy

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    39, 4, 25, 999, 5050, 222333444
]

test_data = [
    3, 0, 2, 4, 1, 4
]


for i, d in enumerate(data):
    assert multiplication_chain(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
