

class Cell:
    def __init__(self):
        self.is_alive = False
        self.neighbors = 0
    
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
        for row in range(self.rows):
            for column in range(self.columns):
                if self.cells[row][column].getAlive():
                    print("*", end="")
                else:
                    print(" ", end="")
            print("")
                
class Game:
    def __init__(self):
        self.board = Board()
        try:
            with open(input("Enter file name: ")) as f:
                lines = f.readlines()

            for row_idx, row in enumerate(lines):
                for col_idx, column in enumerate(row.strip()):
                    if column == '*':
                        self.board.cells[row_idx][col_idx].setAlive()
                        for inc_row in [-1, 0, 1]:
                            for inc_col in [-1, 0, 1]:
                                if inc_row == 0 and inc_col == 0:
                                    continue
                                new_row = row_idx + inc_row
                                new_col = col_idx + inc_col
                                if 0 <= new_row < self.board.rows and 0 <= new_col < self.board.columns:
                                    self.board.cells[new_row][new_col].addNeighbor()

        except FileNotFoundError:
            print("No valid board found")

    def nextGeneration(self):
        for row in range(self.board.rows):
            for col in range(self.board.columns):
                current_cell = self.board.cells[row][col]
                alive_neighbors = current_cell.getNeighbors()
    
                if current_cell.getAlive():
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        current_cell.killCell()  # Rule 1 and 3
                else:
                    if alive_neighbors == 3:
                        current_cell.setAlive()  # Rule 4
    
        # After processing all cells, update neighbor counts
        for row in range(self.board.rows):
            for col in range(self.board.columns):
                current_cell = self.board.cells[row][col]
                if current_cell.getAlive():
                    for inc_row in [-1, 0, 1]:
                        for inc_col in [-1, 0, 1]:
                            if inc_row == 0 and inc_col == 0:
                                continue
                            new_row = row + inc_row
                            new_col = col + inc_col
                            if 0 <= new_row < self.board.rows and 0 <= new_col < self.board.columns:
                                self.board.cells[new_row][new_col].addNeighbor()
    
        # After updating all cells and neighbor counts, reprocess cells for Rule 2
        for row in range(self.board.rows):
            for col in range(self.board.columns):
                current_cell = self.board.cells[row][col]
                alive_neighbors = current_cell.getNeighbors()
                if current_cell.getAlive():
                    if 2 <= alive_neighbors <= 3:
                        continue  # Rule 2, live cell survives
                    else:
                        current_cell.killCell()  # Rule 1 and 3
                else:
                    if alive_neighbors == 3:
                        current_cell.setAlive()  # Rule 4
                    
    def loop(self):
        end = False
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