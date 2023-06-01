# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt

"""
Код читает предложенный файл, удаляет из текста все символы-цифры и выводит результат в новый файл
"""
with open('test_file/task1_data.txt', 'r', encoding='utf-8') as raw_file:
    row_list = raw_file.readlines()
    for row in row_list:
        prepared_row = ''
        for item in range(len(row)):
            if not row[item].isdigit():
                prepared_row += row[item]
        with open('test_file/task1_answer.txt', 'a', encoding='utf-8') as prep_file:
            prep_file.write(prepared_row)


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
