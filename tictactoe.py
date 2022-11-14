import random

# Initialize the board
board = [' ' for x in range(10)]

# Function to insert the letter in the board
def insert_letter(letter, pos):
    board[pos] = letter

# Function to check if the space is free or not
def freeSpace(pos):
    return board[pos] == ' '

# Function to print the board on console
def printBoard(board):
    print("\t-------------")
    print(f"\t| {board[1]} | {board[2]} | {board[3]} |")
    print("\t-------------")
    print(f"\t| {board[4]} | {board[5]} | {board[6]} |")
    print("\t-------------")
    print(f"\t| {board[7]} | {board[8]} | {board[9]} |")
    print("\t-------------")

# Check if the board is full
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

# Check if the player has won or not
def checkWinner(board , letter):
    f1 = (board[1] == letter and board[2] == letter and board[3] == letter)
    f2 = (board[4] == letter and board[5] == letter and board[6] == letter)
    f3 = (board[7] == letter and board[8] == letter and board[9] == letter)
    f4 = (board[1] == letter and board[4] == letter and board[7] == letter)
    f5 = (board[2] == letter and board[5] == letter and board[8] == letter)
    f6 = (board[3] == letter and board[6] == letter and board[9] == letter)
    f7 = (board[1] == letter and board[5] == letter and board[9] == letter)
    f8 = (board[3] == letter and board[5] == letter and board[7] == letter)
    f = f1 or f2 or f3 or f4 or f5 or f6 or f7 or f8
    return f

# Player's turn
def playerRound():
    run = True
    while  run:
        move = input("Please select a position to enter the X between 1 to 9: ")
        # Check if the input is valid or not
        try:
            move = int(move)
            # Check if the input is in range or not
            if move > 0 and move <10:
                # Check if the space is free or not
                if freeSpace(move):
                    run = False
                    insert_letter('X', move)
                else:
                    print("Try again, this space is occupied")
            else:
                print("Please type a no. between 1 and 9")
        # Exception handling   
        except:
            print("Please type a number")

# Computer's turn
def computerRound():
    availableMoves = [x for x , letter in enumerate(board) if letter == " " and x!=0]
    move =0

    # Check for possible winning move to take or to block the player from winning
    for let in ['O', 'X']:
        for i in availableMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if checkWinner(boardcopy, let):
                move = i
                return move

    # Check for corners
    openCorners = []
    for i in availableMoves:
        if i in [1, 3, 7, 9]:
            openCorners.append(i)

    # Check if the corners are free or not
    if len(openCorners) > 0:
        move = randomSelection(openCorners)
        return openCorners[move]

    # Check for the center
    if 5 in availableMoves:
        move = 5
        return move

    openEdges = []
    # Check for the edges
    for i in availableMoves:
        if i in [2, 4, 6, 8]:
            openEdges.append(i)

    # Check if the edges are free or not
    if len(openEdges) >0:
        move = randomSelection(openEdges)
        return openEdges[move]
    return move

# Function for random selection for computer turn
def randomSelection(li):
    # import random
    ln = len(li)
    r = random.randrange(0,ln)
    return r

# Main function
def main():
    print("Welcome to Tic-Tac-Toe Bootleg Edition!")
    print()
    printBoard(board)
    print()

    # Loop for the game
    while not(isBoardFull(board)):
        if not(checkWinner(board, 'O')):
            playerRound()
            printBoard(board)
        else:
            print("Sorry, Game Over!")
            print()
            break
        if not(checkWinner(board, 'X')):
            comp_move = computerRound()
            if comp_move == 0:
                print(" ")
            else:
                insert_letter('O', comp_move)
                print('Computer placed an O on position ', comp_move , ':')
                printBoard(board)

        else:
            print("YOU WIN!")
            print()
            break
          
    if isBoardFull(board):
        print("Game Tied")
        print()

while True:
    x = input("Are you ready to play? (y/n) ")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------------')
        main()
    else:
        break