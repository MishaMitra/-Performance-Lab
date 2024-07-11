# #Задание №1 - Круговой массив

import argparse


def main():
    parser = argparse.ArgumentParser(description="Круговой массив")
    parser.add_argument('-n', type=int, help="Массив числом n (любое целое число)")
    parser.add_argument('-m', type=int, help="Интервал для движения по массиву (любое целое число)")
    args = parser.parse_args()

    if args.n is None:
        n = int(input("Привет, задайте массив числом n (любое целое число): "))
    else:
        n = args.n

    if args.m is None:
        m = int(input("Теперь задайте интервал для движения по массиву (любое целое число): "))
    else:
        m = args.m

    one_Array = m * [int(i) for i in range(1, n + 1)]
    two_Array = [' ']
    three_Array = []
    count = 0

    while two_Array[-1] != 1:
        two_Array.clear()
        for j in range(count, m + count):
            two_Array.append(one_Array[j])
            count += 1
        two_List_copy = two_Array.copy()
        three_Array.append(two_List_copy)
        count -= 1

    print("Полученный путь:")
    for k in range(len(three_Array)):
        print(three_Array[k][0], end='')



main()
