# stuff to run always here such as class/def
class main():
    class TicTacToe:
        def __init__(self, num, symbol):
            self.boardNum = num
            match symbol:
                case "X":
                    self.board = [["X", " ", " ", " ", "X"],
                                  [" ", "X", " ", "X", " "],
                                  [" ", " ", "X", " ", " "],
                                  [" ", "X", " ", "X", " "],
                                  ["X", " ", " ", " ", "X"]]
                case "O":
                    self.board = [[" ", "O", "O", "O", " "],
                                  ["O", " ", " ", " ", "O"],
                                  ["O", " ", " ", " ", "O"],
                                  ["O", " ", " ", " ", "O"],
                                  [" ", "O", "O", "O", " "]]
                case _:
                    self.board = [[" ", "|", " ", "|", " "],
                                  ["—", "|", "—", "|", "—"],
                                  [" ", "|", " ", "|", " "],
                                  ["—", "|", "—", "|", "—"],
                                  [" ", "|", " ", "|", " "]]
            
        def __str__(self):
            returnBoard = ""
            for r in range(len(self.board)):
                for c in range(len(self.board[r])):
                    returnBoard = returnBoard + f"{self.board[r][c]} "
                returnBoard = returnBoard + "\n"
            return returnBoard

        def replaceValue(self, row, col, symbol):
            validRow, validCol = True, True
            if(row == 3):
                row+=1
                validRow = True
            elif(row == 1):
                row-=1
                validRow = True
            elif(row == 2):
                validRow = True
            else:
                print("Invalid row")
                validRow = False

            if(col == 3):
                col+=1
                validCol = True
            elif(col == 1):
                col-=1
                validCol = True
            elif(col == 2):
                validCol = True
            else:
                print("Invalid column")
                validCol = False

            if(validRow is True and validCol is True):
                isPlacementValid = self.confirmPlacement(row, col)
                if(isPlacementValid is True):
                    self.board[row][col] = symbol
                    return True
                else:
                    return False

        def gameOver(self):
            winner = "No one"
            isGameOver = False
            #Player Win
            for r in range(len(self.board)):
                for c in range(len(self.board[r])):
                    symbol = self.board[r][c]
                    if((symbol=="X" or symbol=="O") and 
                      ((self.board[0][0]==self.board[0][2]==self.board[0][4]==symbol or #Right 2; Case 1, 1
                        self.board[0][0]==self.board[2][0]==self.board[4][0]==symbol or #Down 2 
                        self.board[0][0]==self.board[2][2]==self.board[4][4]==symbol) or #Right Diagonal 2
                        self.board[0][2]==self.board[2][2]==self.board[4][2]==symbol or #Down 2; Case 1, 2 
                       (self.board[0][4]==self.board[2][4]==self.board[4][4]==symbol or #Down 2; Case 1, 3 
                        self.board[0][4]==self.board[2][2]==self.board[4][0]==symbol) or #Left Diagonal 2
                        self.board[2][0]==self.board[2][2]==self.board[2][4]==symbol or #Right 2; Case 2, 1
                        self.board[4][0]==self.board[4][2]==self.board[4][4]==symbol)): #Right 2; Case 3, 1

                        '''print(str(self.board[0][0]==self.board[0][2]==self.board[0][4]==symbol), #Right 2; Case 1, 1
                                 str(self.board[0][0]==self.board[2][0]==self.board[4][0]==symbol), #Down 2 
                                 str(self.board[0][0]==self.board[2][2]==self.board[4][4]==symbol), #Right Diagonal 2
                                 str(self.board[0][2]==self.board[2][2]==self.board[4][2]==symbol), #Down 2; Case 1, 2 
                                 str(self.board[0][4]==self.board[2][4]==self.board[4][4]==symbol), #Down 2; Case 1, 3 
                                 str(self.board[0][4]==self.board[2][2]==self.board[4][0]==symbol), #Left Diagonal 2
                                 str(self.board[2][0]==self.board[2][2]==self.board[2][4]==symbol), #Right 2; Case 2, 1
                                 str(self.board[4][0]==self.board[4][2]==self.board[4][4]==symbol))'''
                        isGameOver = True
                        if(symbol=="X"):
                            winner = "Player One"
                        elif(symbol=="O"):
                            winner = "Player Two"
                        break
                    else:
                        continue
                if isGameOver is True:
                    break

            #Draw
            if isGameOver is False:
                for row in range(len(self.board)):
                    for col in range(len(self.board[row])):
                        symbol = self.board[row][col]
                        if(symbol==" "):
                            break
                        else:
                            if(row==4 and col==4):
                                isGameOver = True
                            continue
                    else:
                        continue
                    break
            return isGameOver, winner

        def confirmPlacement(self, row, col):
            if(self.board[row][col]!=" "):
                print("That square is occupied. Please choose another. ")
                return False
            elif(self.board[row][col]==" "):
                return True

if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    main()
    firstBoard = main.TicTacToe(1, "")
    print()
    print(firstBoard)
    hasSomeoneWon = False
    currentTurn = 1
    while(hasSomeoneWon is False):
        if(currentTurn == 1):
            print("Player 1: ")
            player1Row = int(input("Which row do you want to place in? "))
            player1Col = int(input("Which column do you want to place in? "))
            if(firstBoard.replaceValue(player1Row, player1Col, "X") is True):
                pass
            else:
                continue
            print(firstBoard)
            hasSomeoneWon, winner = firstBoard.gameOver()
            if(hasSomeoneWon is True):
                print(winner+" wins!")
                break
            else:
                currentTurn = 2
        if(currentTurn == 2):
            print("\nPlayer 2: ")
            player2Row = int(input("Which row do you want to place in? "))
            player2Col = int(input("Which column do you want to place in? "))
            if(firstBoard.replaceValue(player2Row, player2Col, "O") is True):
                pass
            else:
                continue
            print(firstBoard)
            hasSomeoneWon, winner = firstBoard.gameOver()
            if(hasSomeoneWon is True):
                print(winner+" wins!")
                break
            else:
                currentTurn = 1
        print("\n")