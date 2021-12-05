import os


def reading_pargchomp(lst_sonor_readings, i):
    assert i > 0
    assert i < len(lst_sonor_readings)
    return lst_sonor_readings[i-1] + lst_sonor_readings[i] + lst_sonor_readings[i+1]


def read_input(str_file_name):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    lst_readings = []
    with open(os.path.join(__location__, str_file_name)) as file:
        for line in file:
            lst_readings.append(int(line.rstrip()))
    return lst_readings


def solve1():
    readings = read_input('input.txt')

    counting_increases = 0
    for j in range(1, len(readings)):
        if readings[j - 1] < readings[j]:
            counting_increases += 1

    print(counting_increases)


def solve2():
    readings = read_input('input.txt')
    lst_sum_three_consecutive_readings= []
    for i in range(1, len(readings) - 1):
        lst_sum_three_consecutive_readings.append(reading_pargchomp(readings, i))

    counting_increases = 0

    for j in range(1, len(lst_sum_three_consecutive_readings)):

        if lst_sum_three_consecutive_readings[j -1] < lst_sum_three_consecutive_readings[j]:
            counting_increases += 1

    print(counting_increases)


if __name__ == '__main__':
    solve1()
    solve2()



