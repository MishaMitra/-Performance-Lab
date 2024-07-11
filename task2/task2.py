# #Задание №2 - Программа, которая рассчитывает положение точки относительно
# окружности.
import argparse
import math

# Эта функция читает данные об окружности из нашего файла
def read_circle_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # координаты центра окружности
        x_center, y_center = map(float, lines[0].strip().split())
        # радиус окружности
        radius = float(lines[1].strip())
    return x_center, y_center, radius

# Эта функция читает координаты точек из файла
def read_points(file_path):
    points = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # Каждая строка файла содержит координаты одной точки
        for line in lines:
            x, y = map(float, line.strip().split())
            points.append((x, y))
    return points

# Эта функция определяет положение точки относительно окружности
def point_position(x_center, y_center, radius, x, y):
    distance = math.sqrt((x - x_center) ** 2 + (y - y_center) ** 2)
    if distance == radius:
        return 0  # На окружности
    elif distance < radius:
        return 1  # Внутри окружности
    else:
        return 2  # Снаружи окружности

def main():
    parser = argparse.ArgumentParser(description="Определение положения точки относительно окружности")
    parser.add_argument('-c', '--circle', type=str, help="Путь к файлу с данными об окружности")
    parser.add_argument('-p', '--points', type=str, help="Путь к файлу с координатами точек")
    args = parser.parse_args()

    if args.circle is None:
        circle_file = input("Введите путь к файлу с данными об окружности: ")
    else:
        circle_file = args.circle

    if args.points is None:
        points_file = input("Введите путь к файлу с координатами точек: ")
    else:
        points_file = args.points

    x_center, y_center, radius = read_circle_data(circle_file)
    points = read_points(points_file)

    for x, y in points:
        position = point_position(x_center, y_center, radius, x, y)
        if position == 0:
            print(f"0 - Точка ({x}, {y}) находится на окружности.")
        elif position == 1:
            print(f"1 - Точка ({x}, {y}) находится внутри окружности.")
        else:
            print(f"2 -Точка ({x}, {y}) находится снаружи окружности.")


main()
