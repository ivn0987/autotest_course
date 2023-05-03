# задание 1
square_side = int(input())
perimeter = square_side * 4
area = square_side * square_side
diagonal = square_side * (2 ** (1/2))

print(f'Периметр квадрата равен {perimeter}')
print(f'Площадь квадрата равна {area}')
print(f'Диагональ квадрата равна {diagonal}')

# задание 2
# тут, надеюсь, не будет претензий к названиям переменных?)
number_a = int(input())
number_b = int(input())
number_c = int(input())
Discriminant = (number_b ** 2) - (4 * number_a * number_c)
first_root = (-number_b + (Discriminant ** (1/2))) / (2 * number_a)
second_root = (-number_b - (Discriminant ** (1/2))) / (2 * number_a)
print(f'Первый корень равен {first_root}')
print(f'Второй корень равен {second_root}')

# задание 3
first_string = input()
second_string = input()
final_string = f'{second_string[0]}{second_string[1]}{first_string[2:]} {first_string[0]}{first_string[1]}{second_string[2:]}'
print(final_string)

# задание 4
absolut_path = input()
split_path = absolut_path.split('\\')
disc_name = split_path[0][0]
root_path = split_path[1]
file_name = split_path[-1].split('.')[0]
print(f'Диск {disc_name}')
print(f'Корневая папка {root_path}')
print(f'Имя файла {file_name}')

# задание 5
number_a_in_5_task = int(input())
number_b_in_5_task = int(input())
sum_of_number = f'{number_a_in_5_task} + {number_b_in_5_task} = {number_a_in_5_task + number_b_in_5_task}'
prod = f'{number_a_in_5_task} * {number_b_in_5_task} = {number_a_in_5_task * number_b_in_5_task}'
print(sum_of_number)
print(prod)

# задание 6
string_in_6_task = input()
print(string_in_6_task[1::2])

# задание 7
first_string_in_7_task = input()
second_string_in_7_task = input()
first_symbol = second_string_in_7_task.find(first_string_in_7_task[0])
second_symbol = second_string_in_7_task.find((first_string_in_7_task[1]))
third_symbol = second_string_in_7_task.find(first_string_in_7_task[2])
min_index = min(first_symbol, second_symbol, third_symbol)
max_index = max(first_symbol, second_symbol, third_symbol)
print(f'Минимальный срез {second_string_in_7_task[min_index:max_index+1]}')

