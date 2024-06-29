# #Задание №3 - Программа, которая формирует файл report.json, со структурой tests.json
# и добавляет параметр value из values.json
import json

# Читаем данные из JSON файла
def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
# Записываем их
def write_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Преобразоваем списка значений в словарь для быстрого поиска по ID
def build_values_dict(values):
    values_dict = {}
    for value in values['values']:
        # В этом словаер ключ — это строковое представление ID, значение — число
        values_dict[str(value['id'])] = value
    return values_dict


# Заполненяем поля 'value' для каждого test на основе словаря значений
def fill_values(test, values_dict):
    if str(test['id']) in values_dict:
        # Заполняет значение из словаря
        test['value'] = values_dict[str(test['id'])]['value']
    else:
        # Если ID нет в словаре, устанавливает value как None, на всякий случай
        test['value'] = None

# Назначаем переменные путями к файлам
values_file = 'values.json'
tests_file = 'tests.json'
report_file = 'report.json'
# Читаем из них
values = read_json(values_file)
tests = read_json(tests_file)
# Создаем словарь значений для быстрого поиска
values_dict = build_values_dict(values)
# Зполняем
for test in tests['tests']:
    fill_values(test, values_dict)
# Записываем в report
write_json(tests, report_file)