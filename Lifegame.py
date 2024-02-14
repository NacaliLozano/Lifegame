

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
    

class Board:
    def __init__(self):
        self.rows = 10
        self.columns = 10
        
        self.cells = []
        for row in range(self.rows):
            self.cells.append([])
            for column in range(self.columns):
                self.cells[row].append(Cell())
        

                 
                
class Game:
    def __init__(self):
        try:
            with open("lifegame.txt") as f:
                lines = f.readlines()
            for line in lines:
                for character in line:
                    if character == '*':
                        self.board.cells[line][character].is_alive = True
        
        except:
            print("No board found")
        
            
    def next_generation(self):
        for row in range(self.board.rows):
            for column in range(self.board.columns):
                for increment_rows in [-1, 0, 1]:
                    for increment_columns in [-1, 0, 1]:
                        if row + increment_rows in range(self.board.rows) and column + increment_columns in range(self.board.columns):
                            if increment_rows == 0 and increment_columns == 0:
                                continue
                            elif self.board.cells[row + increment_rows][column + increment_columns].is_alive:
                                self.board.cells[row][column].neighbors += 1
                                
        for row in range(self.board.rows):
            for column in range(self.board.columns):
                if self.board.cells[row][column].is_alive:
                    if self.board.cells[row][column].neighbors < 2 or self.board.cells[row][column].neighbors > 3:
                        self.board.cells[row][column].is_alive = False
                else:
                    if self.board.cells[row][column].neighbors == 3:
                        self.board.cells[row][column].is_alive = True
                        
                        