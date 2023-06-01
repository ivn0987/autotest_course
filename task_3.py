# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

"""
Код считывает из фала список цен, сумммирует по покупкам и записывает в переменную сумму трех самых дорогих
"""
with open('test_file/task_3.txt', 'r', encoding='utf-8') as raw_file:
    row_list = raw_file.readlines()
    price_list = []
    price = 0
    for row in row_list:
        if len(row) > 1:
            price += int(row)
        else:
            price_list.append(price)
            price = 0
    price_list.sort(reverse=True)
three_most_expensive_purchases = sum(price_list[:3])

assert three_most_expensive_purchases == 202346
