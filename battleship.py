import random

class Board:
    def __init__(self):
        self.spaces = [*range(1,101)]
        self.board_spaces = {}
        self.stored_vert_nums = []
        self.stored_hor_nums = []
    
    def __repr__(self):
        return "This is the game board, it contains modules for producing vertical and horizontal pieces, as well as the game board itself!"
    
    def create_ships(self):
        self.destroyer = random.randint(1, 2)
        print(self.destroyer)
        self.submarine = random.randint(1, 2)
        print(self.submarine)
        self.cruiser = random.randint(1, 2)
        print(self.cruiser)
        self.battleship = random.randint(1, 2)
        print(self.battleship)
        self.carrier = random.randint(1, 2)
        print(self.carrier)

        if self.destroyer == 1:
            Board.get_vertical(self, 2)
        else:
            Board.get_horizontal(self, 2)
        if self.submarine == 1:
            Board.get_vertical(self, 3)
        else:
            Board.get_horizontal(self, 3)
        if self.cruiser == 1:
            Board.get_vertical(self, 3)
        else:
            Board.get_horizontal(self, 3)
        if self.battleship == 1:
            Board.get_vertical(self, 4)
        else:
            Board.get_horizontal(self, 4)
        if self.carrier == 1:
            Board.get_vertical(self, 5)
        else:
            Board.get_horizontal(self, 5)
        
    def get_vertical(self, size):
        num = random.randint(1, 100)
        stored_vert_nums = []
        stored_vert_nums.append(num)
        if num >= 60:
            stored_vert_nums.append(num-10)
            if size == 2:
                self.stored_vert_nums.append(stored_vert_nums)
                return
            stored_vert_nums.append(num-20)
            if size == 3:
                self.stored_vert_nums.append(stored_vert_nums)
                return
            stored_vert_nums.append(num-30)
            if size == 4:
                self.stored_vert_nums.append(stored_vert_nums)
                return
            stored_vert_nums.append(num-40)
            self.stored_vert_nums.append(stored_vert_nums)
            return  
        else:
            stored_vert_nums.append(num+10)
            if size == 2:
                self.stored_vert_nums.append(stored_vert_nums)
                return
            stored_vert_nums.append(num+20)
            if size == 3:
                self.stored_vert_nums.append(stored_vert_nums)
                return
            stored_vert_nums.append(num+30)
            if size == 4:
                self.stored_vert_nums.append(stored_vert_nums)
                return
            else:
                stored_vert_nums.append(num+40)
                self.stored_vert_nums.append(stored_vert_nums)
                return

    def get_horizontal(self, size):
        num = random.randint(1, 100)
        stored_hor_nums = []
        stored_hor_nums.append(num)
        if (num % 10 == 0):
            stored_hor_nums.append(num-1)
            if size == 2:
                self.stored_hor_nums.append(stored_hor_nums)
                return 
            stored_hor_nums.append(num-2)
            if size == 3:
                self.stored_hor_nums.append(stored_hor_nums)
                return 
            stored_hor_nums.append(num-3)
            if size == 4:
                self.stored_hor_nums.append(stored_hor_nums)
                return
            stored_hor_nums.append(num-4)
            self.stored_hor_nums.append(stored_hor_nums)
            return
        elif (num % 10 == 9):
            stored_hor_nums.append(num-1)
            if size == 2:
                self.stored_hor_nums.append(stored_hor_nums)
                return 
            stored_hor_nums.append(num-2)
            if size == 3:
                self.stored_hor_nums.append(stored_hor_nums)
                return 
            stored_hor_nums.append(num-3)
            if size == 4:
                self.stored_hor_nums.append(stored_hor_nums)
                return
            stored_hor_nums.append(num-4)
            self.stored_hor_nums.append(stored_hor_nums)
            return
        elif (num % 10 == 8):
            stored_hor_nums.append(num-1)
            if size == 2:
                self.stored_hor_nums.append(stored_hor_nums)
                return 
            stored_hor_nums.append(num-2)
            if size == 3:
                self.stored_hor_nums.append(stored_hor_nums)
                return 
            stored_hor_nums.append(num-3)
            if size == 4:
                self.stored_hor_nums.append(stored_hor_nums)
                return
            stored_hor_nums.append(num-4)
            self.stored_hor_nums.append(stored_hor_nums)
            return
        elif (num % 10 == 7):
            stored_hor_nums.append(num-1)
            if size == 2:
                self.stored_hor_nums.append(stored_hor_nums)
                return 
            stored_hor_nums.append(num-2)
            if size == 3:
                self.stored_hor_nums.append(stored_hor_nums)
                return 
            stored_hor_nums.append(num-3)
            if size == 4:
                self.stored_hor_nums.append(stored_hor_nums)
                return
            stored_hor_nums.append(num-4)
            self.stored_hor_nums.append(stored_hor_nums)
            return
        elif (num % 10 == 6):
            stored_hor_nums.append(num-1)
            if size == 2:
                self.stored_hor_nums.append(stored_hor_nums)
                return 
            stored_hor_nums.append(num-2)
            if size == 3:
                self.stored_hor_nums.append(stored_hor_nums)
                return 
            stored_hor_nums.append(num-3)
            if size == 4:
                self.stored_hor_nums.append(stored_hor_nums)
                return
            stored_hor_nums.append(num-4)
            self.stored_hor_nums.append(stored_hor_nums)
            return
        else:
            stored_hor_nums.append(num+1)
            if size == 2:
                self.stored_hor_nums.append(stored_hor_nums)
                return 
            stored_hor_nums.append(num+2)
            if size == 3:
                self.stored_hor_nums.append(stored_hor_nums)
                return 
            stored_hor_nums.append(num+3)
            if size == 4:
                self.stored_hor_nums.append(stored_hor_nums)
                return
            stored_hor_nums.append(num+4)
            self.stored_hor_nums.append(stored_hor_nums)
            return


board_1 = Board()

board_1.create_ships()

print(board_1.stored_hor_nums)
print(board_1.stored_vert_nums)
