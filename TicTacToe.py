# author: Ayushi Patel

# 3 x 3 board
board = [["   ", "   ", "   "], ["   ", "   ", "   "], ["   ", "   ", "   "]]

# prompts users to enter names
print("LET'S PLAY TIC TAC TOE!")
PlayerX = input("What is the name of the player playing X? ")
PlayerO = input("What is the name of the player playing O? ")
print(PlayerX + " is X!" + "\n" + PlayerO + " is O!")

# draws board in 3 by 3 format
def draw_board():
    print(board[0][0] + "|" + board[0][1] + "|" + board[0][2])
    print("___|___|___")
    print(board[1][0] + "|" + board[1][1] + "|" + board[1][2])
    print("___|___|___")
    print(board[2][0] + "|" + board[2][1] + "|" + board[2][2])
    print("   |   |   ")

# plays game by running through loop and varying player unitl someone wins or else it is a tie
def play():
    for i in range(4):
        makeMove(PlayerX)
        draw_board()
        checkWin(PlayerX)

        makeMove(PlayerO)
        draw_board()
        checkWin(PlayerO)

    makeMove(PlayerX)
    draw_board()
    checkWin(PlayerX)
    print("Tie Game!")

# returns mark X or O according to player
def mark(player):
    if player == PlayerX:
        return " X "
    elif player == PlayerO:
        return " O "

# places mark on the space player picked on the board
def makeMove(player):
    print("It's " + player + "'s turn.")
    row = int(input("What row would you like to place your mark? "))
    column = int(input("What column would you like to place you mark? "))
    if isInvalidInput(row, column) is True:
        makeMove(player)
    if isSpaceFull(row, column) is True:
        makeMove(player)
    else:
        board[row - 1][column - 1] = mark(player)

# returns true if input in in range
def isInvalidInput(row, column):
    if row < 1 or column < 1 or row > 3 or column > 3:
        print("Invalid entry. Enter a number 1, 2 or 3.")
        return True

# returns true if space is full from user's entered row and column
def isSpaceFull(row, column):
    if board[row - 1][column - 1] != "   ":
        print("There is already a mark at this place.")
        return True

# checks to see if user won for vertical, horizontal and diagonal wins. If user won, game ends.
def checkWin(player):
    if board[0][0] is mark(player) and board[1][0] is mark(player) and board[2][0] is mark(player):
        print(player + " wins!")
        exit()
    elif board[0][1] is mark(player) and board[1][1] is mark(player) and board[2][1] is mark(player):
        print(player + " wins!")
        exit()
    elif board[0][2] is mark(player) and board[1][2] is mark(player) and board[2][2] is mark(player):
        print(player + " wins!")
        exit()
    elif board[0][0] is mark(player) and board[0][1] is mark(player) and board[0][2] is mark(player):
        print(player + " wins!")
        exit()
    elif board[1][0] is mark(player) and board[1][1] is mark(player) and board[1][2] is mark(player):
        print(player + " wins!")
        exit()
    elif board[2][0] is mark(player) and board[2][1] is mark(player) and board[2][2] is mark(player):
        print(player + " wins!")
        exit()
    elif board[0][0] is mark(player) and board[1][1] is mark(player) and board[2][2] is mark(player):
        print(player + " wins!")
        exit()
    elif board[2][0] is mark(player) and board[1][1] is mark(player) and board[0][2] is mark(player):
        print(player + " wins!")
        exit()

# run game
play()