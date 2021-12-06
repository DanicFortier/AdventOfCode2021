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
            line = line.split()

    return None


def solve1():

    pass


def solve2():
    pass


if __name__ == "__main__":
    print('Answer problem part 1: ')
    solve1()
    print('Answer problem part 2: ')
    solve2()
