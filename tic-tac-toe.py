def winner(board):

    def all_same(L):
        return L.count(L[0])==len(L) and L[0] != 0
    #Horizontal check
    for row in board:
        if all_same(row):
            print(f"Winner is player{row[0]} via horizonatlly (---)")
            return True
    
    #Vertical check
    for col in range(len(board)):
        check = []
        for row in board:
            check.append(row[0])
        if all_same(check):
            print(f"Winner is player{check[0]} via vertical(|)")
            return True
    
    #leading diagonal check
    diagonal = []
    for i in range(len(board)):
        diagonal.append(board[i][i])
    if all_same(diagonal):
        print(f"Winner is player{diagonal[0]} via diagonally(\\)")
        return True
    
    #Counter diagonal check
    diagonal = []
    for i,j in enumerate(reversed(range(len(board)))):
        diagonal.append(board[i][j])
    if all_same(diagonal):
        print(f"Winner is player{diagonal[0]} via diagonally(/)")
        return True


    
def board_game(game_board, player = 0, row = 0, col = 0, just_display=False):
    try : 
        if game_board[row][col] !=0 :
            print("Already choosen indexes. Please Try again !!!\n")
            return game, False

        if not just_display:
            game_board[row][col] = player
        s = "   "+ "  ".join(str(i) for i in range(len(game)))
        print(s)
        for count, row in enumerate(game_board):
            print(count, row)
        print()
        return game_board, True
    except IndexError as e:
        print("Error : Make sure you enter 0,1 or 2 as row/col =>",e)
        return game, False
    except Exception as e: 
        print("Error : Something gone very wrong =>", e)
        return game, False

# board = board_game(board, just_display=True)
# board = board_game(board, 1,1,1)
# winner(board)

play = True
while play:
    size = 3
    game = [ [ 0 for i in range(size)] for j in range(size) ]
    
    # print("   0  1  2")
    s = "   "+ "  ".join(str(i) for i in range(len(game)))
    print(s)
    for count, row in enumerate(game):
        print(count, row)
        
    game_won = False 
    player = [1,2]
    current_player = 0
    while not game_won:
        current_player = player[(current_player)%2]
        print(f"Current player {current_player}")
        played = False

        while not played: 
            column_choice = int(input("Enter Column number (0,1,2) : "))
            row_choice = int(input("Enter Row number (0,1,2) : "))
            game, played = board_game(game, current_player, row_choice ,column_choice)
        
        if winner(game):
            game_won = True
            again = input("Do you want to play again ? (Y/N)")
            if(again.lower() == 'y'):
                print("\nRestarting.......\n")
            elif again.lower() == 'n':
                print("\nByeeee.......\n")
                play = False
            else :
                print("\nWrong input terminating ......\n")
                play = False

