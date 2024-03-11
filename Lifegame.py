

class Cell:
    def __init__(self):
        self.is_alive = False
    
    def setAlive(self):
        self.is_alive = True
    
    def killCell(self):
        self.is_alive = False
        
    def addNeighbor(self):
        self.neighbors += 1
        
    def removeNeighbor(self):
        self.neighbors -= 1
        
    def getAlive(self):
        return self.is_alive
    
    def getNeighbors(self):
        return self.neighbors
    
class Board:
    def __init__(self):
        self.rows = 10
        self.columns = 10
        
        self.cells = []
        for row in range(self.rows):
            self.cells.append([])
            for column in range(self.columns):
                self.cells[row].append(Cell())
        
    def printBoard(self):
        print(" 0123456789")
        for row in range(self.rows):
            print(row, end="")
            for column in range(self.columns):
                if self.cells[row][column].getAlive():
                    print("*", end="")
                else:
                    print(" ", end="")
            print("")
            
    def getCell(self, row, col):
        if row in range(self.rows) and col in range(self.columns):
            return self.cells[row][col]
        else:
            return None
        
    def getRows(self):
        return self.rows
    
    def getColumns(self):
        return self.columns
    
    def getNeighbors(self, row, col):
        if row not in range(self.rows) or col not in range(self.columns):
            return None
        
        neighbors = 0
        for inc_row in [-1, 0, 1]:
            for inc_col in [-1, 0, 1]:
                if inc_row == 0 and inc_col == 0:
                    continue
                new_row = row + inc_row
                new_col = col + inc_col
                if new_row in range(self.rows) and new_col in range(self.columns):
                    if self.cells[new_row][new_col].getAlive():
                        neighbors += 1
        return neighbors
                
class Game:
    def __init__(self):
        self.board = Board()
        self.aux_board = Board()
        try:
            with open("game.txt") as f:
                lines = f.readlines()
            assert(len(lines) == 10)
            for row_idx, row in enumerate(lines):
                assert(len(row) == 11)
                for col_idx, column in enumerate(row):
                    if column == '*':
                        self.board.getCell(row_idx, col_idx).setAlive()
                        
        except FileNotFoundError:
            print("No board found")

    def nextGeneration(self):
        for row in range(self.board.getRows()):
            for col in range(self.board.getColumns()):
                current_cell = self.board.getCell(row, col)
                aux_cell = self.aux_board.getCell(row, col)
                alive_neighbors = self.board.getNeighbors(row, col)
    
                if current_cell.getAlive():
                    if 2 <= alive_neighbors <= 3:
                        aux_cell.setAlive()  # Rule 2
                else:
                    if alive_neighbors == 3:
                        aux_cell.setAlive()  # Rule 4
                        
        self.board = self.aux_board
        
    def loop(self):
        end = False
        self.board.printBoard()
        while not end:
            entry = input("Type 1 to continue, 0 to end: ")
            if entry == "1":
                self.nextGeneration()
                self.board.printBoard()
            elif entry == "0":
                end = True
            else:
                pass


game = Game()
game.loop()
