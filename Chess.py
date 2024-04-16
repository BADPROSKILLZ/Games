import random
class chessBoard:
    def setUpBoard(self, setUpString: str = "r") -> None:
        """
        Sets up the board as either white or black

        :param setUpString: Decides what color the user will be; Random if nothing entered
        """

        self.color = "r"
        if setUpString in ["r", "random"]:
            pickedColor = random.randint(0, 1) #Random color decision
            if pickedColor == 0:
                setUpString = "b" #Black
            else:
                setUpString = "w" #White
        
        if setUpString in ["b", "black"]:
            setUpString = "♖♘♗♔♕♗♘♖N♙♙♙♙♙♙♙♙N        N        N        N        N♟♟♟♟♟♟♟♟N♜♞♝♚♛♝♞♜E" #Default Black Board Setup
            self.color = "black"
        elif setUpString in ["w", "white"]:
            setUpString = "♜♞♝♛♚♝♞♜N♟♟♟♟♟♟♟♟N        N        N        N        N♙♙♙♙♙♙♙♙N♖♘♗♕♔♗♘♖E" #Default White Board Setup
            self.color = "white"

        self.board = [['re', 're', 're', 're', 're', 're', 're', 're'], ['re', 're', 're', 're', 're', 're', 're', 're'], ['re', 're', 're', 're', 're', 're', 're', 're'], ['re', 're', 're', 're', 're', 're', 're', 're'], ['re', 're', 're', 're', 're', 're', 're', 're'], ['re', 're', 're', 're', 're', 're', 're', 're'], ['re', 're', 're', 're', 're', 're', 're', 're'], ['re', 're', 're', 're', 're', 're', 're', 're']] #re for replace; [[]*8]*8 treated as 8 copies of the same list
        row = 0
        col = 0
        for char in range(0, len(setUpString)):
            if setUpString[char] == "N":
                row += 1
                col = 0
            elif setUpString[char] == "E":
                break
            else:
                self.board[row][col] = setUpString[char]
                col += 1
                #print(self.board, "\n")
        
    def showBoard(self):
        """
        Prints the board to the screen from user perspective
        """

        if self.color == "white":
            print("\n")
            for row in range(len(self.board)):
                for col in range(len(self.board[row])):
                    if col == 0 :
                        print(str(8-row), end="  ")
                    print(self.board[row][col], end="  ")
                
                print("\n")

            print("   a  b  c  d  e  f  g  h\n")
        else:
            print("\n")
            for row in range(len(self.board)):
                for col in range(len(self.board[row])):
                    if col == 0 :
                        print(str(row+1), end="  ")
                    print(self.board[row][col], end="  ")
                
                print("\n")

            print("   h  g  f  e  d  c  b  a\n")
    
    def selectPiece(self, piece: str):
        pass

class pieces:
    pass
    

board = chessBoard()
userColor = ""
colorQuestionCount = 0
while userColor not in ["b", "black", "r", "random", "w", "white"]:
    if colorQuestionCount > 0:
        print("Not a valid board input.")
    
    userColor = input("Which color would you like to be? ").lower()
    colorQuestionCount += 1

board.setUpBoard(userColor)
board.showBoard()