#TicTacToe 10/17/18

#last element 0 when Xs(player) turn, 1 when Os
#max is Xs min is Os
import copy
board3 = [" "," "," "," "," "," "," "," "," ", 0]
board4 = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",  0]

def main(size = 3):
    if size != 3 and size != 4:
        print("You must enter 3 or 4")
        pass

    if size == 3:
        board = board3
        
        play3(board)
       

    if size == 4:
        board = board4
        play4(board)

    
    

def play3(s):
    board = s
    
    endTest = endState(board)
    if endTest != 2 :
        if endTest == 1:
            print("X Wins")
            playing = False
        if endTest == -1:
            print("O Wins")
            playing = False
        if endTest == 0:
            print("Tie")
            playing = False
    else:
        playing = True
    if playing:
       
            printBoard(board)
            
            if board[9] == 0:
                print("your turn, choose your move by typing the number of the square you want, read from top left to bottom right")
                playerMove = input()

                if playerMove == "1":
                    if board[0] == " ":
                        board[0] = "X"
                        board[9] = 1
                        play3(board)
                    else:
                        print("Not a valid move")
                        play3(board)

                if playerMove == "2":
                    if board[1] == " ":
                        board[1] = "X"
                        board[9] = 1
                        play3(board)
                    else:
                        print("Not a valid move")
                        play3(board)

                if playerMove == "3":
                    if board[2] == " ":
                        board[2] = "X"
                        board[9] = 1
                        play3(board)
                    else:
                        print("Not a valid move")
                        play3(board)

                if playerMove == "4":
                    if board[3] == " ":
                        board[3] = "X"
                        board[9] = 1
                        play3(board)
                    else:
                        print("Not a valid move")
                        play3(board)

                if playerMove == "5":
                    if board[4] == " ":
                        board[4] = "X"
                        board[9] = 1
                        play3(board)
                    else:
                        print("Not a valid move")
                        play3(board)

                if playerMove == "6":
                    if board[5] == " ":
                        board[5] = "X"
                        board[9] = 1
                        play3(board)
                    else:
                        print("Not a valid move")
                        play3(board)

                if playerMove == "7":
                    if board[6] == " ":
                        board[6] = "X"
                        board[9] = 1
                        play3(board)
                    else:
                        print("Not a valid move")
                        play3(board)

                if playerMove == "8":
                    if board[7] == " ":
                        board[7] = "X"
                        board[9] = 1
                        play3(board)
                    else:
                        print("Not a valid move")
                        play3(board)

                if playerMove == "9":
                    if board[8] == " ":
                        board[8] = "X"
                        board[9] = 1
                        play3(board)
                    else:
                        print("Not a valid move")
                        play3(board)

            else:
               AIMove = miniMaxDecision(board)
               play3(AIMove)
    print("GAME OVER")

def miniMaxDecision(s):
    levelCounter = 0
    
    actionsList = minActions(s)
    
    for action in actionsList:
        printBoard(action)
        if minValue(action) == -1:
            print("Computer move:")
            return action
    for action in actionsList:
        if minValue(action) == 0:
            print("Computer Move:")
            return action
    else:
        print("Computer Move:")
        return action
        
    
def minValue(s):
    #test if win state, if it is return this one
    #print("minvalue")
    util = endState(s)
    if util != 2:
        return util
    else:
        #If not a win state generate the next set of moves
        minActionsList = maxActions(s)
        for action in minActionsList:

            actionValue = maxValue(action)
            if actionValue == 1:
                return actionValue
        for action in minActionsList:
            actionValue = maxValue(action)
            if actionValue == 0:
                return actionValue
        for action in minActionsList:
            actionValue = maxValue(action)
            return actionValue
    
        

def maxValue(s):
    #test if win state, if it is return this one
    #print("maxvalue")
    util = endState(s)
    if util != 2:
        return util
    else:
        #If not a win state generate the next set of moves
        maxActionsList = minActions(s)
        for action in maxActionsList:
            actionValue = minValue(action)
            if actionValue == -1:
                return actionValue
        for action in maxActionsList:
            actionValue = minValue(action)
            if actionValue == 0:
                return actionValue
        for action in maxActionsList:
            actionValue = minValue(action)
            return actionValue
    
    


def minActions(s):
    actionsList = []
    
    for i in range(0,9):
        board = copy.copy(s)
        if board[i] == " ":
            board[i] = "O"
            board[9] = 0
            actionsList.append(board)
    for x in actionsList:
        pass
        #printBoard(x)
    #print("")
    return actionsList

def maxActions(s):
    actionsList = []
    
    for i in range(0,9):
        board = copy.copy(s)
        if board[i] == " ":
            board[i] = "X"
            board[9] = 1
            actionsList.append(board)
    
    for x in actionsList:
        pass
        #printBoard(x)
    #print("")
    return actionsList

def play4(s):
    board = s
    
    endTest = endState4(board)
    if endTest != 2 :
        if endTest == 1:
            print("X Wins")
            playing = False
        if endTest == -1:
            print("O Wins")
            playing = False
        if endTest == 0:
            print("Tie")
            playing = False
    else:
        playing = True
    if playing:
       
            printBoard4(board)
            
            if board[16] == 0:
                print("your turn, choose your move by typing the number of the square you want, read from top left to bottom right")
                playerMove = input()

                if playerMove == "1":
                    if board[0] == " ":
                        board[0] = "X"
                        board[16] = 1
                        play4(board)
                    else:
                        print("Not a valid move")
                        play4(board)

                if playerMove == "2":
                    if board[1] == " ":
                        board[1] = "X"
                        board[16] = 1
                        play4(board)
                    else:
                        print("Not a valid move")
                        play4(board)

                if playerMove == "3":
                    if board[2] == " ":
                        board[2] = "X"
                        board[16] = 1
                        play4(board)
                    else:
                        print("Not a valid move")
                        play4(board)

                if playerMove == "4":
                    if board[3] == " ":
                        board[3] = "X"
                        board[16] = 1
                        play4(board)
                    else:
                        print("Not a valid move")
                        play4(board)

                if playerMove == "5":
                    if board[4] == " ":
                        board[4] = "X"
                        board[16] = 1
                        play4(board)
                    else:
                        print("Not a valid move")
                        play4(board)

                if playerMove == "6":
                    if board[5] == " ":
                        board[5] = "X"
                        board[16] = 1
                        play4(board)
                    else:
                        print("Not a valid move")
                        play4(board)

                if playerMove == "7":
                    if board[6] == " ":
                        board[6] = "X"
                        board[16] = 1
                        play4(board)
                    else:
                        print("Not a valid move")
                        play4(board)

                if playerMove == "8":
                    if board[7] == " ":
                        board[7] = "X"
                        board[16] = 1
                        play4(board)
                    else:
                        print("Not a valid move")
                        play4(board)

                if playerMove == "9":
                    if board[8] == " ":
                        board[8] = "X"
                        board[16] = 1
                        play4(board)
                    else:
                        print("Not a valid move")
                        play4(board)
                if playerMove == "10":
                    if board[9] == " ":
                        board[9] = "X"
                        board[16] = 1
                        play4(board)
                    else:
                        print("Not a valid move")
                        play4(board)

                if playerMove == "11":
                    if board[10] == " ":
                        board[10] = "X"
                        board[9] = 1
                        play4(board)
                    else:
                        print("Not a valid move")
                        play4(board)

                if playerMove == "12":
                    if board[11] == " ":
                        board[11] = "X"
                        board[9] = 1
                        play4(board)
                    else:
                        print("Not a valid move")
                        play4(board)

                if playerMove == "13":
                    if board[12] == " ":
                        board[12] = "X"
                        board[16] = 1
                        play4(board)
                    else:
                        print("Not a valid move")
                        play4(board)

                if playerMove == "14":
                    if board[13] == " ":
                        board[13] = "X"
                        board[16] = 1
                        play4(board)
                    else:
                        print("Not a valid move")
                        play4(board)

                if playerMove == "15":
                    if board[14] == " ":
                        board[14] = "X"
                        board[16] = 1
                        play4(board)
                    else:
                        print("Not a valid move")
                        play4(board)

                if playerMove == "16":
                    if board[15] == " ":
                        board[15] = "X"
                        board[16] = 1
                        play4(board)
                    else:
                        print("Not a valid move")
                        play4(board)


            else:
               AIMove = miniMaxDecision4(board)
               play4(AIMove)
    print("GAME OVER")

def miniMaxDecision4(s):
    levelCounter = 0
    
    actionsList = minActions4(s)
    
    for action in actionsList:
        printBoard4(action)
        if minValue4(action) == -1:
            print("Computer move:")
            return action
    for action in actionsList:
        if minValue4(action) == 0:
            print("Computer Move:")
            return action
    else:
        print("Computer Move:")
        return action

def minValue4(s):
    #test if win state, if it is return this one
    #print("minvalue")
    util = endState4(s)
    if util != 2:
        return util
    else:
        #If not a win state generate the next set of moves
        minActionsList = maxActions4(s)
        for action in minActionsList:

            actionValue = maxValue4(action)
            if actionValue == 1:
                return actionValue
        for action in minActionsList:
            actionValue = maxValue4(action)
            if actionValue == 0:
                return actionValue
        for action in minActionsList:
            actionValue = maxValue4(action)
            return actionValue

def maxValue4(s):
    #test if win state, if it is return this one
    #print("maxvalue")
    util = endState4(s)
    if util != 2:
        return util
    else:
        #If not a win state generate the next set of moves
        maxActionsList = minActions4(s)
        for action in maxActionsList:
            actionValue = minValue4(action)
            if actionValue == -1:
                return actionValue
        for action in maxActionsList:
            actionValue = minValue4(action)
            if actionValue == 0:
                return actionValue
        for action in maxActionsList:
            actionValue = minValue4(action)
            return actionValue

def minActions4(s):
    actionsList = []
    
    for i in range(0,16):
        board = copy.copy(s)
        if board[i] == " ":
            board[i] = "O"
            board[16] = 0
            actionsList.append(board)
    for x in actionsList:
        pass
        #printBoard(x)
    #print("")
    return actionsList

def maxActions4(s):
    actionsList = []
    
    for i in range(0,16):
        board = copy.copy(s)
        if board[i] == " ":
            board[i] = "X"
            board[16] = 1
            actionsList.append(board)
    
    for x in actionsList:
        pass
        #printBoard(x)
    #print("")
    return actionsList

def endState(s):
    #returns 1 if x wins, -1 if O wins, 0 if a tie, 2 if the game is not over yet
    if s[0] == "X" and s[1] == "X" and s[2] == "X":
        return 1
    if s[0] == "X" and s[3] == "X" and s[6] == "X":
        return 1
    if s[0] == "X" and s[4] == "X" and s[8] == "X":
        return 1
    if s[1] == "X" and s[4] == "X" and s[7] == "X":
        return 1
    if s[2] == "X" and s[5] == "X" and s[8] == "X":
        return 1
    if s[3] == "X" and s[4] == "X" and s[5] == "X":
        return 1
    if s[2] == "X" and s[4] == "X" and s[6] == "X":
        return 1
    if s[6] == "X" and s[7] == "X" and s[8] == "X":
        return 1

    if s[0] == "O" and s[1] == "O" and s[2] == "O":
        return -1
    if s[0] == "O" and s[3] == "O" and s[6] == "O":
        return -1
    if s[0] == "O" and s[4] == "O" and s[8] == "O":
        return -1
    if s[1] == "O" and s[4] == "O" and s[7] == "O":
        return -1
    if s[2] == "O" and s[5] == "O" and s[8] == "O":
        return -1
    if s[3] == "O" and s[4] == "O" and s[5] == "O":
        return -1
    if s[2] == "O" and s[4] == "O" and s[6] == "O":
        return -1
    if s[6] == "O" and s[7] == "O" and s[8] == "O":
        return -1

    if " " not in s:
        return 0

    else:
        return 2

def endState4(s):
    #returns 1 if x wins, -1 if O wins, 0 if a tie, 2 if the game is not over yet
    if s[0] == "X" and s[1] == "X" and s[2] == "X" and s[3] == "X":
        return 1
    if s[4] == "X" and s[5] == "X" and s[6] == "X" and s[7] == "X":
        return 1
    if s[8] == "X" and s[9] == "X" and s[10] == "X" and s[11] == "X":
        return 1
    if s[12] == "X" and s[13] == "X" and s[11] == "X" and s[15] == "X":
        return 1
    if s[0] == "X" and s[4] == "X" and s[8] == "X" and s[12] == "X":
        return 1
    if s[1] == "X" and s[5] == "X" and s[9] == "X" and s[13] == "X":
        return 1
    if s[2] == "X" and s[6] == "X" and s[10] == "X" and s[14] == "X":
        return 1
    if s[3] == "X" and s[7] == "X" and s[11] == "X" and s[15] == "X":
        return 1
    if s[0] == "X" and s[5] == "X" and s[10] == "X" and s[15] == "X":
        return 1
    if s[3] == "X" and s[6] == "X" and s[9] == "X" and s[12] == "X":
        return 1
    

    if s[0] == "O" and s[1] == "O" and s[2] == "O" and s[3] == "O":
        return -1
    if s[4] == "O" and s[5] == "O" and s[6] == "O" and s[7] == "O":
        return -1
    if s[8] == "O" and s[9] == "O" and s[10] == "O" and s[11] == "O":
        return -1
    if s[12] == "O" and s[13] == "O" and s[11] == "O" and s[15] == "O":
        return -1
    if s[0] == "O" and s[4] == "O" and s[8] == "O" and s[12] == "O":
        return -1
    if s[1] == "O" and s[5] == "O" and s[9] == "O" and s[13] == "O":
        return -1
    if s[2] == "O" and s[6] == "O" and s[10] == "O" and s[14] == "O":
        return -1
    if s[3] == "O" and s[7] == "O" and s[11] == "O" and s[15] == "O":
        return -1
    if s[0] == "O" and s[5] == "O" and s[10] == "O" and s[15] == "O":
        return -1
    if s[3] == "O" and s[6] == "O" and s[9] == "O" and s[12] == "O":
        return -1
    

    if " " not in s:
        return 0

    else:
        return 2

def printBoard(board):
    print("__" + board[0] + "__|__" + board[1] + "__|__" + board[2] + "__")
    print("__" + board[3] + "__|__" + board[4] + "__|__" + board[5] + "__")
    print("    " + board[6] + "   |    " + board[7] + "   |   " + board[8] + "  ")
    
def printBoard4(board):
    print("    " + board[0] + "__|__" + board[1] + "__|__" + board[2] +  "__|__" + board[3] + "   ")
    print("    " + board[4] + "__|__" + board[5] + "__|__" + board[6] + "__|__" + board[7] + "   ")
    print("    " + board[8] + "__|__" + board[9] + "__|__" + board[10] + "__|__" + board[11]+ "  ")
    print("    " + board[8] + "   |    " + board[9] + "   |   " + board[10] + "   |   " + board[11]+ "  ")
