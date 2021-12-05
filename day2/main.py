import os
import sys



def readInput(str_filename):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    output = []
    with open(os.path.join(__location__, str_filename)) as file:
        for line in file:
            line = line.rstrip()
            lst = line.split(' ')
            lst = [lst[0], int(lst[1])]
            output.append(lst)

    return output


def solve1():
    input = readInput("input.txt")

    depth = 0
    forward = 0

    for element in input:
        if element[0] == 'up':
            depth -= element[1]
        if element[0] == 'down':
            depth += element[1]
        if element[0] == 'forward':
            forward += element[1]


    print(depth * forward)


def solve2():
    input = readInput("input.txt")

    depth = 0
    forward = 0
    aim = 0
    for element in input:
        if element[0] == 'up':
            aim -= element[1]
        if element[0] == 'down':
            aim += element[1]
        if element[0] == 'forward':
            forward += element[1]
            depth += aim * element[1]

    print(depth * forward)


if __name__ == "__main__":
   solve1()
   solve2()
