SIZE = 3
import copy
import random

class Player:

    def __init__(self, sign, human_or_AI):
        self.sign_board = sign
        self.human_or_AI = human_or_AI

    # function that take a move from person/computer
    # return the move number
    # ckeck if between validetion
    # if between 0-8 \ if place in board empty
    def get_move(self, game):
        #if play with person
        if self.human_or_AI == "person":
            # enter a move
            move_player = input("What is youre move ? :  ")
            # move between 0-8?
            if int(move_player) > 8 and int(move_player) < 0:
                print ("input must be between 0-8")
                return -1
            # move place is empty ?
            if (game.board[int(move_player)] != " "):
                print("That place is not empty - try again ")
                move_player = input("What is youre move ? :  ")
                if int(move_player) > 8 and int(move_player) < 0:
                    print ("input must be between 0-8")
                    return -1
            # if all the checking pass
            return int(move_player)
        # if play with the computer
        if self.human_or_AI == "computer":
            empty_cell = self.availspots(game.board)
            depth = len(empty_cell)
            if depth == 0 or game.finish(None) == "X" or game.finish(None) == "O":
                return
            # move by minimax algoritem
            move = self.minimax(game,depth,"O")
            return move[0]

    # function that culculate all the open moves in the board .
    # return a list of the open moves
    def availspots(self, board):
        empty_cell = []
        for i in range(SIZE * 3):
            if board[i] == " ":
                empty_cell.append(i)
        return empty_cell

    # if winner is player 1 score = 1
    # if winner is player 2 score = 2
    # if no one win score = 0
    def eavluate(self, game):
        if game.finish(None) == "O":
            score = +1
        elif game.finish(None) == "X":
            score = -1
        else:
            score = 0
        return score

    def minimax(self, game, depth, player):

        if player == "O":
            best = [-1, -10000000]
        else:
            best = [-1, 10000000]

        if depth == 0 or game.finish(None) == "X" or game.finish(None) == "O":
            score = self.eavluate(game)
            return [-1, score]

        for cell in self.availspots(game.board):
            game.board[cell] = player

            if player == "O":
                score = self.minimax(game,depth-1,"X")
            else:
                score = self.minimax(game,depth-1,"O")

            game.board[cell] = " "
            score[0] = cell

            if player == "O":
                if best[1] < score[1]:
                    best = score
            else:
                if best[1] > score[1]:
                    best = score

        return best

class Game():
    # properties : board , player 1 , player 2 is person if press 2 else is AI
    def __init__(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.player1 = Player("X", "person")
        print ("Enter your opponent's type : computer or person ")
        print("Computer press---------- 1 ")
        print ("Person press -----------2 ")
        type = input("Enter number _____")
        if type == "1":
            self.player2 = Player("O", "computer")
        else:
            self.player2 = Player("O", "person")

    # the the board in the pormt
    # ---  ---  ---
    # |     |    |    |
    #  ---  ---  ---
    # |     |    |    |
    #  ---  ---  ---
    # |     |    |    |
    #  ---  ---  ---
    def draw_board(self):
        line1 = " --- " * SIZE
        for i in range(0, 9, 3):
            print (line1)
            line2 = "|  " + str(self.board[i]) + "  |  " + str(self.board[i+1]) + " |  " + str(self.board[i+2]) + " |  "
            print (line2)
        print (line1)

    # print the game law
    def print_law(self):
        board_cordinate = ["0 1 2", "3 4 5", "6 7 8"]
        print ("                 ")
        print ("player 1 is -----X")
        print ("player 2 is -----O")
        print ("                 ")
        print ("player 1 is first")
        print ("the borad input is like that ")
        print (board_cordinate[0])
        print (board_cordinate[1])
        print (board_cordinate[2])
        print ("                 ")
        return 0

    # checking if someone win the game
    # return the sign_tav of the player that win ,otherwise return 0
    def finish(self, test):
        # row win situation
        if test != None:
            self.board = copy.copy(test)
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] == "X":
                return self.board[i]
            if self.board[i] == self.board[i+1] == self.board[i+2] == "O":
                return self.board[i]
        # column win situeation
        for i in range(0, SIZE):
            if self.board[i] == self.board[i+3] == self.board[i+6] == "X":
                return self.board[i]
            if self.board[i] == self.board[i+3] == self.board[i+6] == "O":
                return self.board[i]
        # diagonal win situation
        if self.board[0] == self.board[4] == self.board[8] == "X":
            return self.board[0]
        if self.board[0] == self.board[4] == self.board[8] == "O":
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] == "X":
            return self.board[2]
        if self.board[2] == self.board[4] == self.board[6] == "O":
            return self.board[2]
        return 0

    # run the play and checking
    # get input
    # checking winners ?
    def run(self,test):
        if test == None:
            for i in range(0, 9):
                if i % 2 == 0:
                    move1 = self.player1.get_move(self)
                    self.board[move1] = "X"
                    if move1 == -1:
                        return 0
                else:
                    move2 = self.player2.get_move(self)
                    if move2 == -1:
                        return 0
                    self.board[move2] = "O"
                self.draw_board()

                if self.finish(None) == "X":
                    print ("Player1  is the WINNER")
                    return 0

                if self.finish(None) == "O":
                    print ("Player2 is the WINNER")
                    return 0

            print ("No WINNER")
            return 0
        else:
            self.board = test
            start = self.player1.availspots(self.board)
            for i in range(9-len(start), 9):
                if i % 2 == 0:
                    while 1:
                        j = random.randrange(0, 8)
                        if self.board[j] == " ":
                            move1 = j
                            break
                    self.board[move1] = "X"
                    if move1 == -1:
                        return 0
                else:
                    move2 = self.player2.get_move(self)
                    if move2 == -1:
                        return 0
                    self.board[move2] = "O"
                if self.finish(None) == "X":
                    print ("Player1  is the WINNER")
                    return 0

                if self.finish(None) == "O":
                    print ("Player2 is the WINNER")
                    return 0

            print ("No WINNER")
            return 0


# run the code
board = Game()
board.print_law()
board.draw_board()
board.run(None)