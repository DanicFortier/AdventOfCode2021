import os

def readInput(str_filename):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    int_lst = []
    with open(os.path.join(__location__, str_filename)) as file:
        for line in file:
            int_lst.append(line.rstrip())


    return int_lst

def bin_to_dec(lst_bin):
    summ = 0
    for i in range(len(lst_bin)):
        summ += int(lst_bin[len(lst_bin) - i - 1]) * 2**i
    return summ



def co2_analyse_rec(lst_numbers, bit_index):
    # Returns the filtered list of numbers
    
    if len(lst_numbers) == 1:
        lst = []
        for i in lst_numbers[0]:
            lst.append(i)
        return lst

    summ = 0
    for num in lst_numbers:
        summ += int(num[bit_index])

    avg = summ / len(lst_numbers)


    if avg < 0.5:
        lp = 1
    else:
        lp = 0

    result = []
    for num in lst_numbers:
        if int(num[bit_index]) == lp:
            result.append(num)
    
    return co2_analyse_rec(result, bit_index + 1)


def o2_analyse_rec(lst_numbers, bit_index):
    # Returns the filtered list of numbers

    if len(lst_numbers) == 1:
        lst = []
        for i in lst_numbers[0]:
            lst.append(i)
        return lst

    summ = 0
    for num in lst_numbers:
        summ += int(num[bit_index])

    avg = summ / len(lst_numbers)

    if avg >= 0.5:
        mp = 1
    else:
        mp = 0

    result = []
    for num in lst_numbers:
        if int(num[bit_index]) == mp:
            result.append(num)
    
    return o2_analyse_rec(result, bit_index + 1)


def solve1():

    input = readInput('input.txt')
    BINARY_LENGTH = len(input[0])

    summs = [0] * BINARY_LENGTH

    for str_num in input:
        for i in range(BINARY_LENGTH):
            summs[i] += int(str_num[i])

    gamma = [round(x / len(input)) for x in summs]
    epsilion = [0 if x == 1 else 1 for x in gamma]
    print(bin_to_dec(gamma) * bin_to_dec(epsilion))


def solve2():
    input = readInput('input.txt')
    o2_rating = bin_to_dec(o2_analyse_rec(input, 0))
    co2_rating = bin_to_dec(co2_analyse_rec(input, 0))

    print(o2_rating * co2_rating)


if __name__ == "__main__":
    print('Answer problem part 1: ')
    solve1()
    print('Answer problem part 2: ')
    solve2()
