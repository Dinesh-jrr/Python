import random
import os.path
import json
random.seed()


def draw_board(board):
    print("  " + board[7] + " |  " +  board[8] + "  |" + board[9])
    print("---------------")
    print("  " + board[4] + " |  " +  board[5] + "  |" + board[6])
    print("---------------")
    print("  " + board[1] + " |  " +  board[2] + "  |" + board[3])
board=[" "," "," "," "," "," "," "," "," "," "]
draw_board(board)
pass
def welcome(board):
    print("Welcome to the \"Unbeatable Noughts and Crosses\" game.\n The board layout is shown below.")
    print("When prompted,enter the number corresponding to the square you want.")
welcome(board)
pass

def initialise_board(board):
    # develop code to set all elements of the board to one space ' '
    board=[]
    for i in range(9):
        board.append(" ")
    return (board)
initialise_board(board)
    
def get_player_move(board):
    # develop code to ask the user for the cell to put the X in,
    # and return row and col
    while True:
        move = input("Enter the cell to put X in (1-9): ")
        if move.isdigit() and int(move) in range(1, 10):
            index = int(move)
            row = (index - 1) // 3
            col = (index - 1) % 3
            if board[index] == ' ':
                return row, col
            else:
                print("Cell already occupied, please choose another cell.")
        else:
            print("Invalid input, please enter a valid cell (1-9).")

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
row, col = get_player_move(board)
print(f"Selected cell: row={row}, col={col}")


def choose_computer_move(board):
#     # develop code to let the computer chose a cell to put a nought in
#     # and return row and col
    def minimax(depth,player,alpha,beta):
        winner=get_player_move(board)
        if winner is not None:
            if winner=="O":
                return 1
            elif winner =="X":
                return -1
            else:
                return 0
    return row, col


def check_for_win(board, mark):
    # develop code to check if either the player or the computer has won
    # return True if someone won, False otherwise
    for row in range(3):
        if board[row][0]== board[row][1] == board[row][2]==mark:
            return True
    for col in range(3):
        if board[0][col]==board[1][col]==board[2][col]==mark:
            return True
    if board[0][0] == board[1][1]== board[2][2]==mark:
        return True
    if board[0][2] == board[1][1]== board[2][0]==mark:
        return True
    return False
check_for_win(board,mark)

def check_for_draw(board):
    # develop cope to check if all cells are occupied
    # return True if it is, False otherwise
    for row in range(3):
        for col in range(3):
            if board[row][col]=="":
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
    #repeat the loop
    while True:
        get_player_move(board)
        draw_board(board)
        if check_for_win(board, "X"):
            return 1
        if check_for_draw(board):
            return 0
        row,col = choose_computer_move(board)
        board[row][col]="O"

        draw_board(board)
        if check_for_win(board,"O"):
            return -1
        if check_for_draw(board):
            return 0
    return 0
play_game(board)                 
                
def menu():
    # get user input of either '1', '2', '3' or 'q'
    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program
    print("Menu:")
    print("1.Play the game")
    print("2.Save score in file'Leaderboard.txt'")
    print("Load and display the score from the l'leaderboard.txt'")
    print("q:Quit")
    #get user input
    choice=input("Enter your choice:")
    while choice not in['1','2','3','q']:
        print("Invalid choice.Please enter'1','2','3' or 'q'")
        choice=input("Enter your choice:")
    return choice

def load_scores():
    # develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # return the scores in a Python dictionary
    # with the player names as key and the scores as values
    # return the dictionary in leaders
    try:
        with open("leaderboard.txt","r") as f:
            leaders={}
            for line in f:
                name,score=line.strip().split(',')
                leaders[name]=int(score)
            return leaders
    except FileNotFoundError:
        print("Leaderboard file not found.")
        return {}
    return leaders
load_scores()


def save_score(score):
    # develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'

    #get the player name
    name=input("Enter your name:")
    #write the score to the file
    with open("leaderboard.txt","w") as f:
        f.write(name + ","+str(score)+"\n")
    print("Score saved")
    return score

# score=100 # example for score value
save_score(100)

def display_leaderboard(leaders):
    # develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader
    if not leaders:
        print("Not scores found")
        return
    print("leaderboard:")
    for name,score in leaders.items():
        print(f"{name}:{score}")
    return
    pass
