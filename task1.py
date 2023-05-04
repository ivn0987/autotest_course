# Напишите функцию modification(lst), которая принимает список и меняет местами его первый и последний элемент.
# В исходном списке минимум 2 элемента.

def modification(lst):
    first_el = lst[0]
    last_el = lst[-1]
    lst.append(first_el)
    lst.pop(-2)
    lst.insert(0, last_el)
    lst.pop(1)
    # Здесь нужно написать код
    return lst

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    [1, 2, 3],
    [1, 2, 3, 4, 5],
    ['н', 'л', 'о', 'с']
]

test_data = [
    [3, 2, 1], [5, 2, 3, 4, 1], ['с', 'л', 'о', 'н']
]


for i, d in enumerate(data):
    assert modification(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
