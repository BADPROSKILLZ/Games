#Make Super Tic Tac Toe
from TicTacToe import main

object = main()

class SuperTicTacToe:
    def __init__(self):
        self.stringBoards = {}
        self.boards = [object]*10
        for i in range(0, 9):
            i+=1
            self.boards[i] = object.TicTacToe(i, "")
            self.stringBoards[i] = str(self.boards[i])

    def __str__(self):
        #Variable Declaration
        returnString = ""
        stringBoards = str(list(self.stringBoards.values())) + " " #Store entire values array as a string
        #print(stringBoards+"\n\n\n")
        stringBoards = stringBoards.replace(", ", "").replace("[", "").replace("]", "").replace("\'", "").replace("\\n", "") #Remove Unnecessary Characters
        stringBoards = stringBoards[:len(stringBoards)-1]
        boards = stringBoards
        stringArray = []
        boardPart = 0
        count = 0
        standardArray = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39] #Not end-of-line segments
        newlineArray = [10, 11, 12, 13, 25, 26, 27, 28, 40, 41, 42, 43] #End-of-line segments
        newBoardArray = [14, 29, 44] #End-of-board-row segments

        #Set every index of stringArray as the 10 corresponding characters in stringBoards
        for index in range(int(len(boards)/10)):
            stringArray.append(boards[:10])
            boards = boards.replace(stringArray[index], "", 1)

        #Add 10-character board segment
        while(count<=int(len(stringBoards)/10)):
            if(boardPart in standardArray):
                #print(f"boardPart: {boardPart}")
                returnString = returnString +  stringArray[boardPart] + "❚ "
                boardPart += 5
            elif(boardPart in newlineArray):
                #print(f"boardPart: {boardPart}")
                returnString = returnString +  stringArray[boardPart] + "\n"
                boardPart -= 9
            elif(boardPart in newBoardArray):
                #print(f"boardPart: {boardPart}")
                returnString = returnString +  stringArray[boardPart] + "\n"
                if(boardPart == 14 or boardPart == 29):
                    returnString = returnString + "==========❚===========❚==========\n"
                boardPart+=1
            count+=1

        return returnString

    def playOnBoard(self, num, row, col, symbol):
        valueIsReplaced = False
        while(valueIsReplaced is False):
            valueIsReplaced = self.boards[num].replaceValue(row, col, symbol)
            if(valueIsReplaced is False):
                row, col = 0, 0
                print("\n")
                while(row==0):
                    try:
                        row = int(input("Which row do you want to play on? "))
                    except ValueError:
                        print("Enter a number 1-3\n")
                        row = 0
                    else:
                        if(row>3 or row<1):
                            print("Enter a number 1-3\n")
                            row = 0
                while(col==0):
                    try:
                        col = int(input("Which column do you want to play on? "))
                    except ValueError:
                        print("Enter a number 1-3\n")
                        col = 0
                    else:
                        if(col>3 or col<1):
                            print("Enter a number 1-3\n")
                            col = 0
        self.stringBoards[num] = str(self.boards[num])
        return row, col

    def boardWin(self, num, symbol):
        isBoardWon, winner = self.boards[num].gameOver()
        if isBoardWon is True:
            match symbol:
                case "X":
                    self.boards[num] = object.TicTacToe(num, "X") #make an X
                case "O":
                    self.boards[num] = object.TicTacToe(num, "O") #make a circle
            self.stringBoards[num] = str(self.boards[num])

    def isBoardPlaceable(self, num):
        if(self.stringBoards[num].encode()==b'  O O O   \nO       O \nO       O \nO       O \n  O O O   \n'):
            return False, "O"
        elif(self.stringBoards[num].encode()==b'X       X \n  X   X   \n    X     \n  X   X   \nX       X \n'):
            return False, "X"
        else:
            return True, ""
    
    def hasGameEnded(self):
        #Player Win
        boardWinners = [""]*10
        for r in range(len(boardWinners)-1):
            r+=1
            placeability, winner = bigBoard.isBoardPlaceable(r)
            boardWinners[r] = winner
            
        if(boardWinners[1]==boardWinners[2]==boardWinners[3]!="" or #Right 2; Case 1, 1
           boardWinners[1]==boardWinners[4]==boardWinners[7]!="" or #Down 2 
           boardWinners[1]==boardWinners[5]==boardWinners[9]!="" or #Right Diagonal 2
           boardWinners[2]==boardWinners[5]==boardWinners[8]!="" or #Down 2; Case 1, 2 
           boardWinners[3]==boardWinners[6]==boardWinners[9]!="" or #Down 2; Case 1, 3 
           boardWinners[3]==boardWinners[5]==boardWinners[7]!="" or #Left Diagonal 2
           boardWinners[4]==boardWinners[5]==boardWinners[6]!="" or #Right 2; Case 2, 1
           boardWinners[7]==boardWinners[8]==boardWinners[9]!=""):  #Right 2; Case 3, 1
            return True, "w" #Win case
        elif(boardWinners[1]!="" and 
            boardWinners[2]!="" and
            boardWinners[3]!="" and
            boardWinners[4]!="" and
            boardWinners[5]!="" and
            boardWinners[6]!="" and
            boardWinners[7]!="" and
            boardWinners[8]!="" and
            boardWinners[9]!=""):
            return True, "d" #Draw case
        else:
            return False, "n" #Not over yet
bigBoard = SuperTicTacToe()
isGameOver = False
currentBoard = 0
currentRow = 0
currentColumn = 0
currentPlayer = "X"
symbol = "X"
canPlace = True
print(bigBoard)
while(isGameOver is not True):
    if(currentBoard!=0):
        canPlace, boardWinner = bigBoard.isBoardPlaceable(currentBoard)
    while(currentBoard == 0 or canPlace is False):
        try:
            currentBoard = int(input("Which board do you want to play on? "))
        except ValueError:
            print("Enter a number from 1-9\n")
        else:
            if(currentBoard>0 and currentBoard<10):
                canPlace, boardWinner = bigBoard.isBoardPlaceable(currentBoard)
            else:
                print("Enter a number from 1-9\n")
                currentBoard = 0
    
    print(f"\nPlayer {currentPlayer} is now playing on board {currentBoard}.")
    while(currentRow==0):
        try:
            currentRow = int(input("Which row do you want to play on? "))
        except ValueError:
            print("Enter a number from 1-3\n")
        else:
            if(currentRow<=0 or currentRow>=4):
                print("Enter a number from 1-3\n")
                currentRow = 0
                
    while(currentColumn==0):
        try:
            currentColumn = int(input("Which column do you want to play on? "))
        except ValueError:
            print("Enter a number from 1-3\n")
        else:
            if(currentColumn<=0 or currentColumn>=4):
                print("Enter a number from 1-3\n")
                currentColumn = 0
                
    currentRow, currentColumn = bigBoard.playOnBoard(currentBoard, currentRow, currentColumn, symbol)
    bigBoard.boardWin(currentBoard, symbol)
    print(bigBoard)
    match currentRow:
        case 1:
            match currentColumn:
                case 1:
                    currentBoard = 1
                case 2:
                    currentBoard = 2
                case 3:
                    currentBoard = 3
        case 2:
            match currentColumn:
                case 1:
                    currentBoard = 4
                case 2:
                    currentBoard = 5
                case 3:
                    currentBoard = 6
        case 3:
            match currentColumn:
                case 1:
                    currentBoard = 7
                case 2:
                    currentBoard = 8
                case 3:
                    currentBoard = 9

    isGameOver, winDraw = bigBoard.hasGameEnded()
    currentRow, currentColumn = 0, 0
    if(isGameOver is True and winDraw=="w"):
        print(f"Player {currentPlayer} won!")
    elif(isGameOver is True and winDraw=="d"):
        print("The game is a draw!")
    
    if(currentPlayer == "X"):
        symbol, currentPlayer = "O", "O"
    else:
        symbol, currentPlayer = "X", "X"