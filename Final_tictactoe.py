import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board): #Display of a Board on which the game will be played
    clear_screen()
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('------')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('------')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('\n')

def space_available(position): #Check whether the space is available or not on the position we entered
    return board[position] == ' '

def make_move(letter, position): #Function to make a move either by a player or by AI
    if space_available(position):
        board[position] = letter
        print_board(board)

    if check_draw():
        print("It's a draw!")
        exit()

    if check_for_win():
        if letter == 'X':
            print("AI Bot wins!")
            exit()
        else:
            print("Player wins!")
            exit()

def check_draw():
    return all(board[key] != ' ' for key in board.keys())

def check_for_win():
    win_conditions = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (7, 5, 3)]
    for a,b,c in win_conditions:
        if(board[a] == board[b] == board[c] and board[a] != ' '):
            return True
    return False

def check_which_mark_won(mark): #To find for beating the player
    win_conditions = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (7, 5, 3)]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] == mark:
            return True
    return False

def player_move(): #This function defines the player moves with error handling
    while True:
        try:
            position = int(input("Enter the position for 'O':  "))
            if position in board and space_available(position):
                make_move(player, position)
                break
            else:
                print("Invalid move! Position already taken or out of range.")
        except ValueError:
            print("Please enter a valid number.")

def ai_move(): #This Function defines the ai moves which is based on minimax algorithm
    best_score = -800
    best_move = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = bot
            score = minimax(board, 0, False, -800, 800)
            board[key] = ' '
            if score > best_score:
                best_score = score
                best_move = key
    make_move(bot, best_move)

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_which_mark_won(bot):
        return 1
    elif check_which_mark_won(player):
        return -1
    elif check_draw():
        return 0

    if is_maximizing:
        best_score = -800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = bot
                score = minimax(board, 0, False, alpha, beta)
                board[key] = ' '
                best_score = max(best_score, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = 800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, 0, True, alpha, beta)
                board[key] = ' '
                best_score = min(best_score, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return best_score

player = 'O'
bot = 'X'
board= {1: ' ', 2: ' ', 3: ' ',
        4: ' ', 5: ' ', 6: ' ',
        7: ' ', 8: ' ', 9: ' '}

print_board(board)
while not check_for_win():
    ai_move()
    if not check_for_win():
        player_move()
