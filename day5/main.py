import os
import sys



def readInput(str_filename):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    returned_list = []

    max_x=0
    max_y = 0
    with open(os.path.join(__location__, str_filename)) as file:
        for line in file:
            line = line.rstrip()
            line = line.split(' -> ')

            p1 = line[0].split(',')
            p2 = line[1].split(',')

            x1 = int(p1[0])
            y1 =int(p1[1])

            x2 = int(p2[0])
            y2 = int(p2[1])

            max_x = max(max_x, x1, x2)
            max_y = max(max_y, y1, y2)

            line = ([x1, y1], [x2, y2])

            returned_list.append(line)

            size = (max_x, max_y)
    return returned_list, size


def add_line_to_matrix(matrix, line):

    x1, y1 = line[0]
    x2, y2 = line[1]

    direction = ''
    if x1 == x2:
        direction = 'vertical'

    elif y1 == y2:
        direction = 'horizontal'

    else:
        direction = 'diagonal'

    if direction == 'horizontal':
        if x1 < x2:
            #GOING LEFT
            x2, x1 = x1, x2

        for i in range(x2, x1 + 1):
            matrix[y1][i] += 1

    if direction == 'vertical':
        if y1 < y2:
            # going up
            y2, y1 = y1, y2
        for i in range(y2, y1 + 1):
            matrix[i][x1] += 1

    if direction == 'diagonal':
        if y1 > y2:
            x2, x1 = x1, x2
            y2, y1 = y1, y2

        while y1 <= y2:
            if x1 < x2:
                matrix[y1][x1] += 1
                x1 +=1
            else:
                matrix[y1][x1] += 1
                x1 -= 1
            y1 += 1


def counting_interesting_dots(matrix):
    summ = 0
    for row in matrix:
        for elem in row:
            if elem > 1:
                summ += 1
    return summ


def init_matrix(size):
    matrix = [[0] * 1000 for i in range(1000)]

    return matrix


def solve1():

    input, size = readInput('input.txt')

    matrix = init_matrix(size)

    for line in input:
        add_line_to_matrix(matrix, line)

    answer = counting_interesting_dots(matrix)

    print(answer)

def solve2():
    pass



if __name__ == "__main__":
    print('Answer problem part 1: ')
    solve1()
    print('Answer problem part 2: ')
    solve2()
