import os
import sys
from day4.sequence import sequence
from day4.sequence import sequence_test


def readInput():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    boards = []
    with open(os.path.join(__location__,'input.txt')) as file:
        board_lst = []                
        for line in file:
            if line == '\n': #If line is empty
                board = False
            else:
                board = True
            
            if board:
                row = line.rstrip().split(' ')
                new_lst = [int(x) for x in row if x != '']
                board_lst.append(new_lst)
            if not board:
                boards.append(board_lst)
                board_lst = []
    
    boards.append(board_lst)
    return boards
                 
def board_to_dict(board):
    board_dict = {}
    nb_rows = len(board)
    nb_columns = len(board[0])

    for i in range(nb_rows):
        for j in range(nb_columns):
            num = board[i][j]
            board_dict[num] = (i, j)

    return board_dict

def init_board(board):
    for i in range(len(board)):
            for j in range(len(board[0])):
                num = board[i][j]
                board[i][j] = [num, False]

# Returns the score if the column has a bingo, otherwise returns false
def check_col(board, int_col):
    summ = 0
    for row in board:
        if not row[int_col][1]:
            return False

    return True

# Returns the score if the row has a bingo, otherwise returns false
def check_row(board, int_row):
    # [[48, False], [69, False], [68, True], [49, False], [13, True]]
    row = board[int_row]

    for e in row:
        if not e[1]:
            return False

    return True

# Returns the score if the board has a bingo, otherwise returns false
def check_winner(board):
    
    for i in range(len(board)):
        res = check_row(board, i)
        # If res is a score and not False. res is a int. btw a number greater than 0 is Truthy
        if res:
            return res

    for i in range(len(board[0])):
        res = check_col(board, i)
        # If res is a score and not False
        if res:
            return res

    return False

def sum_of_unmarked(board):
    summ = 0
    for row in board:
        for cell in row:
            if not cell[1]:
                summ += cell[0] 
    return summ


def check_if_everyboard_won(lst_board_won):
    return all(lst_board_won)


def solve1():
    boards = readInput()

    lst_board_dict = []

    for board in boards:
        lst_board_dict.append(board_to_dict(board))
        init_board(board)

    for number in sequence:
        board_number = 0
        for dict_board in lst_board_dict:
            if number in dict_board:
                x, y = dict_board[number]
                boards[board_number][x][y][1] = True
                
            # Check if winner winner chicken dinner
            result = check_winner(boards[board_number])
            if result:
                score_of_board = sum_of_unmarked(boards[board_number])
                return score_of_board * number

            board_number += 1


def solve2():
    boards = readInput()

    lst_board_dict = []

    lst_board_won = [False] * len(boards)

    boards_sums = []
    for board in boards:
        lst_board_dict.append(board_to_dict(board))
        init_board(board)
    
        
        
    for number in sequence:
        board_number = 0
        for dict_board in lst_board_dict:
            if number in dict_board:
                x, y = dict_board[number]
                boards[board_number][x][y][1] = True
                
            # Check if winner winner chicken dinner
            result = check_winner(boards[board_number])
            if result:
                lst_board_won[board_number] = True
                if check_if_everyboard_won(lst_board_won):
                    return sum_of_unmarked(boards[board_number]) * number
                #score_of_board = sum_of_unmarked(boards[board_number])
                #return score_of_board * number

            board_number += 1


if __name__ == "__main__":
    print(solve2())
