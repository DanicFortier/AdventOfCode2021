# Returns the score if the column has a bingo, otherwise returns false
def check_col(board, int_col):
    summ = 0
    for row in board:
        if not row[int_col][1]:
            return False
        else:
            summ += row[int_col][0]

    return summ

# Returns the score if the row has a bingo, otherwise returns false
def check_row(board, int_row):
    # [[48, False], [69, False], [68, True], [49, False], [13, True]]
    row = board[int_row]
    summ = 0

    for e in row:
        if not e[1]:
            return False
        else:
            summ += e[0]
    return summ
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

def sum_of_board(board):
    summ = 0
    for row in board:
        summ += sum(row) 
    return summ

board = [
    [[48, True], [69, True], [68, False], [49, True], [13, True]],
    [[25, True], [14, True], [30, True], [74, True], [89, False]],
    [[16, True], [38, False], [19, True], [24, False], [29, True]],
    [[56, True], [97, False], [50, True], [65, True], [79, True]],
    [[57, True], [52, True], [5, False], [27, True], [76, True]]
]

board_1 = [
    [1, 2],
    [3, 4]
]

print(sum_of_board(board_1))
