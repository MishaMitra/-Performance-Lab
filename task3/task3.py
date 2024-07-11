# #Задание №3 - Программа, которая формирует файл report.json, со структурой tests.json
# и добавляет параметр value из values.json
import argparse
import json

# Читаем данные из JSON файла
def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Записываем данные в JSON файл
def write_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Преобразование списка значений в словарь для быстрого поиска по ID
def build_values_dict(values):
    values_dict = {}
    for value in values['values']:
        # В этом словаре ключ — это строковое представление ID, значение — число
        values_dict[str(value['id'])] = value
    return values_dict

# Заполнение полей 'value' для каждого test на основе словаря значений
def fill_values(test, values_dict):
    if str(test['id']) in values_dict:
        # Заполняет значение из словаря
        test['value'] = values_dict[str(test['id'])]['value']
    else:
        # Если ID нет в словаре, устанавливает value как None, на всякий случай
        test['value'] = None

def main():
    parser = argparse.ArgumentParser(description="Заполнение полей value в тестах на основе значений из словаря")
    parser.add_argument('-v', '--values', type=str, help="Путь к файлу со значениями")
    parser.add_argument('-t', '--tests', type=str, help="Путь к файлу с тестами")
    parser.add_argument('-r', '--report', type=str, help="Путь к файлу для сохранения отчета")
    args = parser.parse_args()

    if args.values is None:
        values_file = input("Введите путь к файлу со значениями: ")
    else:
        values_file = args.values

    if args.tests is None:
        tests_file = input("Введите путь к файлу с тестами: ")
    else:
        tests_file = args.tests

    if args.report is None:
        report_file = input("Введите путь к файлу для сохранения отчета: ")
    else:
        report_file = args.report

    # Читаем данные из файлов
    values = read_json(values_file)
    tests = read_json(tests_file)

    # Создаем словарь значений для быстрого поиска
    values_dict = build_values_dict(values)

    # Заполняем поля value в тестах
    for test in tests['tests']:
        fill_values(test, values_dict)

    # Записываем данные в отчет
    write_json(tests, report_file)

if __name__ == "__main__":
    main()
