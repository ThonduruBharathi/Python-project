# TIC TOK TOE
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
current_player = "X"
gameisgoing = True
winner=None
# Displaying board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def handle_turn():
    position = int(input("Enter the position from 0 to 8 :"))
    board[position] = current_player
def swap_players():
    global current_player
    if current_player== "X" :
        current_player= "O"
    elif current_player == "O":
         current_player = "X"
def who_is_winner():
    global winner
    row_winner = check_row()
    col_winner = check_col()
    diag_winner = check_diag()
    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    else:
        winner = diag_winner


# check row
def check_row():
    row1 = board[0]==board[1]==board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        gameisgoing = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
# check column
def check_col():
    global gameisgoing
    col1 = board[0]==board[3]==board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    if col1 or col2 or col3:
        gameisgoing = False
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
def check_diag():
    global gameisgoing
    diag1 = board[0]==board[4]==board[8] != "-"
    diag2 = board[2] == board[4] == board[6] != "-"
    if diag1 or diag2 :
        gameisgoing = False
    if diag1:
        return board[0]
    elif diag2:
        return board[2]


def play_game():
    while gameisgoing:
        display_board()
        handle_turn()
        swap_players()
        who_is_winner()
        if winner == "X":
           print("X is the winner")
        elif winner == "O":
             print("O is the winner")

play_game()