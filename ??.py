# board = [[i for i in table[0:3]], [i for i in table[3:6]], [i for i in table[6:9]]]
board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]


def transpose_board():  # transposes the board to match user input
    for i in range(len(board)):
        for j in range(len(board[0])):
            if j <= i:
                board[i][j], board[j][i] = board[j][i], board[i][j]


def shift_columns(board_length):  # swaps columns and rows to match user input
    # right_col = board_length - 1
    # left_col = 0
    # while board_length > 1:
    #     board[left_col], board[right_col] = board[right_col], board[left_col]
    #     left_col += 1
    #     right_col -= 1
    #     board_length -= 2
    k = 0
    for i in range(len(board)):
        board[i][0], board[i][len(board) - 1] = board[i][len(board) - 1], board[i][0]


def check_valid_input(x, y):  # checks whether the user input is valid
    nums = '1234567890'
    if not x[0] in nums or not y[0] in nums:
        return False, 'You should enter numbers!'
    elif int(x) > len(board) or int(y) > len(board):
        return False, 'Coordinates should be from 1 to 3!'
    elif not board[int(x) - 1][int(y) - 1] == "_":
        return False, 'This cell is occupied! Choose another one!'
    return True, None


def update_pos(x, y, char):  # updates the positions on the board
    board[x - 1][y - 1] = char


def check_win(letter):  # checks the status of the game
    d = check_diagnal()
    if d[0] and d[1] == letter:
        return True
    for i in range(len(board)):
        c = check_col(i)
        r = check_row(i)
        if (r[0] and r[1] == letter) or (c[0] and c[1] == letter):
            return True



def check_empty():  # checks for empty spaces in the board
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "_":
                return True
    return False


def check_row(j):  # checks for a win in the columns of the board
    if board[j][0] == board[j][1] and board[j][1] == board[j][2]:
        return True, board[j][0]
    else:
        return False, None


def check_col(i):  # checks columns of the board for a win
    if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
        return True, board[0][i]
    else:
        return False, None


def check_diagnal():  # checks diagnals of the board for a win
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return True, board[0][0]
    if board[2][0] == board[1][1] and board[1][1] == board[0][2]:
        return True, board[2][0]

    return False, None


def check_sums():  # checks to make sure there aren't more Xs than Os
    num_X = 0
    num_O = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "X":
                num_X += 1
            elif board[i][j] == "O":
                num_O += 1
            else:
                pass

    return (num_X - num_O >= 2) or (num_O - num_X >= 2)


def gen_board(board):  # generates an the image of the board for printing
    txt = ""
    txt += "---------\n"
    for i in range(len(board)):
        txt += "| "
        for j in range(len(board[0])):
            txt += board[i][j] + " "
        txt += "|\n"
    txt += "---------\n"
    return txt


def check_game_status():
    if (check_win("O") and check_win("X")) or (check_sums()):
        return "Impossible"
    elif check_win("O"):
        return "O wins"
    elif check_win("X"):
        return "X wins"
    elif not check_win("O") and not check_win("X") and not check_empty():
        return "Draw"
    else:
        return "Game not finished"


def get_coordinates(player):  # gets coordinates for next position, takes 'X' or 'O' as arg
    coordinates = input(f'{player}, enter coordinates: ')
    return (coordinates.split()[0]), (coordinates.split()[1])


def main():
    round = 0
    while check_game_status() == "Game not finished":
        print(gen_board(board))
        if round % 2 == 0:  # figures out who's turn it is
            letter = "X"
            x, y = get_coordinates(letter)
        else:
            letter = "O"
            x, y = get_coordinates(letter)
        transpose_board()
        shift_columns(len(board))
        if check_valid_input(x, y)[0]:  # checks if user input is correct
            x, y = int(x), int(y)
            update_pos(x, y, letter)
            shift_columns(len(board))
            transpose_board()
        else:
            print(check_valid_input(x, y)[1])
            shift_columns(len(board))
            transpose_board()
            continue
        round += 1
    print(gen_board(board))
    print(check_game_status())





def __main__():
    # while check_game_status() == "Game not finished":
    print(gen_board(board))
    run = True
    while run:
        x, y = get_coordinates("X")
        shift_columns(len(board))
        if check_valid_input(x, y)[0]:
            x = int(x)
            y = int(y)
            update_pos(x, y, 'X')
            shift_columns(len(board))
            print(gen_board(board))
            run = False
        else:
            print(check_valid_input(x, y)[1])
            shift_columns(len(board))



main()


