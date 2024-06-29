# #Задание №4 - Программа, выводящая в консоль минимальное количество ходов, требуемых для
# приведения всех элементов массива к одному числу.


# Читаем чисела из файла и возвращаем их в виде списка целых чисел
def read_numbers(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file]


# Ищем среднее значение из списка
def calculate_median(nums):
    nums.sort()
    n = len(nums)
    mid = n // 2
    if n % 2 == 0:
        # Если количество чисел четное, медиана — это любое значение между двумя элементами в центре
        return (nums[mid - 1] + nums[mid]) // 2
    else:
        # Если количество чисел нечетное, медиана — это элемент по-центру
        return nums[mid]



# Ищем минимальное количество ходов, чтобы привести все чисела к медиане
def calculate_minimum_moves(nums):
    median = calculate_median(nums)
    return sum(abs(num - median) for num in nums)

# Основная функция
def main():
    # Задаем путь к файлу с нашими числами
    file_path = 'numbers.txt'

    # Чтение чисел из файла
    numbers = read_numbers(file_path)

    # Считаем ходы с помощью функции calculate_minimum_moves
    result = calculate_minimum_moves(numbers)

    # Вывод результата
    print(f"Привести все элементы к одному числу можно за : {result} ходов")


# Запускаем нашу машину
main()
