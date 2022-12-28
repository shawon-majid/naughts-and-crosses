import random
import os.path
import json
random.seed()


def draw_board(board):
    # develop code to draw the board
    row = [
        ' ----------- ',
        '| '+str(board[0][0])+' | '+str(board[0][1]) +
        ' | '+str(board[0][2])+' |',
        ' ----------- ',
        '| '+str(board[1][0])+' | '+str(board[1][1]) +
        ' | '+str(board[1][2])+' |',
        ' ----------- ',
        '| '+str(board[2][0])+' | '+str(board[2][1]) +
        ' | '+str(board[2][2])+' |',
        ' ----------- ',
    ]

    for x in row:
        print(x)


def welcome(board):
    # prints the welcome message
    # display the board by calling draw_board(board)

    print('Welcome to the \"Unbeatable Noughts & Crosses\" game.')
    print('The board layout is shown below:')

    draw_board(board)

    print('When prompted, enter the number corresponding to the square you want')


def initialise_board(board):
    # develop code to set all elements of the board to one space ' '
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
    return board


def get_player_move(board):
    # develop code to ask the user for the cell to put the X in,
    print('                   1 2 3')
    print('                   4 5 6')
    X = int(input('Choose Your Square 7 8 9: '))
    X = X - 1
    row = X / 3
    col = X % 3

    # and return row and col
    return int(row), int(col)


def isFree(board, r, c):
    if board[r][c] == ' ':
        return True
    return False


def minimax(board, mark):
    # add terminal case
    copy = board

    if check_for_draw(copy):
        return 0, [-1, -1]
    if check_for_win(copy, 'x'):
        return 1, [-1, -1]
    if check_for_win(copy, 'o'):
        return -1, [-1, -1]

    if mark == 'x':
        mx = -1
        r = -2
        c = -2
        for i in range(1, 10):
            row = int((i - 1) / 3)
            col = int((i - 1) % 3)
            if isFree(copy, row, col):
                copy[row][col] = 'x'
                if minimax(copy, 'o')[0] > mx:
                    mx = minimax(copy, 'o')[0]
                    r = row
                    c = col
                copy[row][col] = ' '
        return mx, [r, c]
    else:
        mn = 1
        r = -3
        c = -3
        for i in range(1, 10):
            row = int((i - 1) / 3)
            col = int((i - 1) % 3)
            if isFree(copy, row, col):
                copy[row][col] = 'o'
                if minimax(copy, 'x')[0] < mn:
                    mn = minimax(copy, 'x')[0]
                    r = row
                    c = col
                copy[row][col] = ' '
        return mn, [r, c]


def choose_computer_move(board):
    # develop code to let the computer chose a cell to put a nought in
    # and return row and col
    return minimax(board, 'o')[1]


def check_for_win(board, mark):
    # develop code to check if either the player or the computer has won

    # win horizontally
    ret = True
    for i in range(3):
        ret = True
        for j in range(3):
            if board[i][j] != mark:
                ret = False
        if ret == True:
            return True

    # win vertically
    for i in range(3):
        ret = True
        for j in range(3):
            if board[j][i] != mark:
                ret = False
        if ret == True:
            return True

    # win via left to right cross
    ret = True
    for i in range(3):
        if board[i][i] != mark:
            ret = False

    if ret == True:
        return True

    # win via right to left cross
    ret = True
    j = 2
    for i in range(3):
        if board[i][j] != mark:
            ret = False
        j = j-1

    return ret
    # return True if someone won, False otherwise


def check_for_draw(board):
    # develop cope to check if all cells are occupied
    # return True if it is, False otherwise
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False

    return True


def play_game(board):
    # develop code to play the game
    # star with a call to the initialise_board(board) function to set
    # the board cells to all single spaces ' '
    # then draw the board
    # then in a loop, get the player move, update and draw the board
    # check if the player has won by calling check_for_win(board, mark),
    # if so, return 1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    # if not, then call choose_computer_move(board)
    # to choose a move for the computer
    # update and draw the board
    # check if the computer has won by calling check_for_win(board, mark),
    # if so, return -1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    # repeat the loop

    initialise_board(board)
    draw_board(board)

    while True:
        r, c = get_player_move(board)
        board[r][c] = 'x'
        draw_board(board)
        if check_for_win(board, 'x'):
            return 1

        if check_for_draw(board):
            return 0

        r, c = choose_computer_move(board)
        board[r][c] = 'o'
        draw_board(board)
        if check_for_win(board, 'o'):
            return -1

        if check_for_draw(board):
            return 0

    return 0


def menu():
    # get user input of either '1', '2', '3' or 'q'
    print('Enter one of the following options:')
    print('\t\t\t1 - Play the game')
    print('\t\t\t2 - Save score in file \'leaderboard.txt\'')
    print('\t\t\t3 - Load and display the scores from the \'leaderboard.txt\'')
    print('\t\t\tq - End the program')

    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program
    choice = input('1, 2, 3 or q? ')

    return choice


def load_scores():
    # develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # return the scores in a Python dictionary
    # with the player names as key and the scores as values
    # return the dictionary in leaders

    f = open("leaderboard.txt", "r")
    leaders = json.loads(f.read())
    f.close()
    return leaders


def save_score(score):
    # develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'

    f = open("leaderboard.txt", "r")
    leaders = json.loads(f.read())
    f.close()

    name = input("Please Enter your name: ")

    leaders[name] = score

    res = json.dumps(leaders)

    f = open("leaderboard.txt", "w")
    f.write(res)
    f.close

    return


def display_leaderboard(leaders):
    # develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader

    print("THE LEADERBOARD")

    for name, score in leaders.items():
        print(name + ' :', score)
