#---------GLOBAL VARIABLES--------

#gameboard
board=["-","-","-",
       "-","-","-",
       "-","-","-"] 


game_still_going=True 



winner=None


current_player="X"

def display_board():
    print (board[0] + "|" + board[1]+ "|" + board[2])
    print (board[3] + "|" + board[4]+ "|" + board[5])
    print (board[6] + "|" + board[7]+ "|" + board[8])


#Play a game of TIC TAC TOE
def play_game():
    display_board() 
   
    while game_still_going:
        #handle turn of player
        handle_turn(current_player)
        #check if game has ended
        check_if_game_over() 
        #flip to the other player
        flip_player() 
    #game has ended 
    if winner== "X" or winner=="O":
        print(winner+"won.")
    elif winner ==None: 
        print("Tie.")
#Hanle a single turn of player
def handle_turn(player):
    
    print(player +"'s turn.") 
    position= input ("Choose a pos from 1-9:")
    valid=False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Error! Choose a position from 1-9:")
        position=int(position) -1 
        if board[position] =="-":
            valid=True 
        else:
            print("NONE SHALL PASS!")
    
    board[position]= player 
    display_board()

def check_if_game_over(): 
    check_for_winner()
    check_if_tie()


def check_for_winner():
    global winner
    row_winner=check_rows()
    col_winner=check_col()
    diag_winner=check_diags()
    if row_winner:
        winner=row_winner
    elif col_winner:
        winner=col_win
    elif diag_winner:
        winner = diag_winner
    else:
        winner=None
    return

def check_rows():
    #Set up global variables
    global game_still_going
    #check row values = same
    row_1=board[0]==board[1]==board[2] !="-"
    row_2=board[3]==board[4]==board[5] !="-"
    row_3=board[6]==board[7]==board[8] !="-"
    #if any row does have a match, flag a win
    if row_1 or row_2 or row_3:
        game_still_going=False
    #Return the winner (X or O)
    if row_1:
        return board[0]
    elif row_2:   
        return board[3]
    elif row_3:  
        return board[6]
    return
def check_col():
    #Set up global variables 
    global game_still_going
    #check col value= same
    col_1=board[0]==board[3]==board[6] !="-"
    col_2=board[1]==board[4]==board[7] !="-"
    col_3=board[2]==board[5]==board[8] !="-"
    #if any row does have a match, flag a win 
    if col_1 or col_2 or col_3: 
        game_still_going=False
    #Return the winner (X or O)
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return

def check_diags():
    #Set up global variables 
    global game_still_going
    #check diag value= same
    diag_1=board[0]==board[4]==board[8] !="-" 
    diag_2=board[2]==board[4]==board[6] !="-"
    #if any diag does have a match, flag a win
    if diag_1 or diag_2:
        game_still_going=False
    #Return the winner (X or O) 
    if diag_1:
        return board[0]
    elif diag_2:
        return board[2]
    return

def check_if_tie():
  global game_still_going
  if "-" not in board:
      game_still_going=False
  return

def flip_player():
    #global variables needed
    global current_player
    #if current player was x, then change to O
    if current_player=="X":
        current_player="O"
    #if current player was o, then change to X
    elif current_player=="O":
        current_player="X"
    return
play_game()


#board 
#display board 
#Play game 
#handle turn
#check win 
    #check rows 
    #check collums
    #check diagonals 
#check tie 
#flip player 