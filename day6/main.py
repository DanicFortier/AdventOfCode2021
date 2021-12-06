import os
import sys
from collections import defaultdict

lanternfish = [3,1,5,4,4,4,5,3,4,4,1,4,2,3,1,3,3,2,3,2,5,1,1,4,4,3,2,4,2,4,1,5,3,3,2,2,2,5,5,1,3,4,5,1,5,5,1,1,1,4,3,2,3,3,3,4,4,4,5,5,1,3,3,5,4,5,5,5,1,1,2,4,3,4,5,4,5,2,2,3,5,2,1,2,4,3,5,1,3,1,4,4,1,3,2,3,2,4,5,2,4,1,4,3,1,3,1,5,1,3,5,4,3,1,5,3,3,5,4,2,3,4,1,2,1,1,4,4,4,3,1,1,1,1,1,4,2,5,1,1,2,1,5,3,4,1,5,4,1,3,3,1,4,4,5,3,1,1,3,3,3,1,1,5,4,2,5,1,1,5,5,1,4,2,2,5,3,1,1,3,3,5,3,3,2,4,3,2,5,2,5,4,5,4,3,2,4,3,5,1,2,2,4,3,1,5,5,1,3,1,3,2,2,4,5,4,2,3,2,3,4,1,3,4,2,5,4,4,2,2,1,4,1,5,1,5,4,3,3,3,3,3,5,2,1,5,5,3,5,2,1,1,4,2,2,5,1,4,3,3,4,4,2,3,2,1,3,1,5,2,1,5,1,3,1,4,2,4,5,1,4,5,5,3,5,1,5,4,1,3,4,1,1,4,5,5,2,1,3,3]
lanternfish_test = [3,4,3,1,2]


def add_day_dict(dict_fish):

    next_day_fish = defaultdict(int)
    new_mature_fish = 0

    for (key, value) in dict_fish.items():
        if key == 0:
            next_day_fish[8] = value
            new_mature_fish += value
        else:
            next_day_fish[key - 1] = value

    next_day_fish[6] += new_mature_fish

    return next_day_fish


def solve1():

    dict_fish = defaultdict(int)

    for timer in lanternfish:
        dict_fish[timer] += 1

    for _ in range(80):
        dict_fish = add_day_dict(dict_fish)

    print(count_number_of_lanternfish(dict_fish))


def count_number_of_lanternfish(dict_fish):
    return sum(dict_fish.values())


def solve2():

    dict_fish = defaultdict(int)

    for timer in lanternfish:
        dict_fish[timer] += 1

    for _ in range(256):
        dict_fish = add_day_dict(dict_fish)

    print(count_number_of_lanternfish(dict_fish))


if __name__ == "__main__":
    print('Answer problem part 1: ')
    solve1()
    print('Answer problem part 2: ')
    solve2()
