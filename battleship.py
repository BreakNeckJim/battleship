import random

class Board:
    def __init__(self):
        self.spaces = [*range(1,101)]
        self.board_spaces = [[' '] * 10 for x in range(10)]
        self.stored_vert_nums = []
        self.stored_hor_nums = []
        self.letters_to_numbers = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10}
        
    def print_board(board):
        row_num = 1
        print("   A B C D E F G H I J")
        while row_num < 10:
            print(str(row_num) + " " + "|_|_|_|_|_|_|_|_|_|_|")
            row_num += 1
        print(str(10) + "|_|_|_|_|_|_|_|_|_|_|")
        

    def __repr__(self):
        return "This is the game board, it contains modules for producing vertical and horizontal pieces, as well as the game board itself!"
    
    def display_board(self):
        pass

    def get_ship_location(self,):
        row = input("Please enter a row 1-10 ")
        while row not in "123456789 10":
            print("Please enter a valid row ")
            row = input("Please enter a row 1-10 ")
        column = input("Please enter a column A-J ").upper()
        while column not in "ABCDEFGHIJ":
            print("Please enter a valid column ")
            column = input("Please enter a column A-J ").upper()
        self.coordinate = (int(row)-1)*10 + int(self.letters_to_numbers[column])
        print(self.coordinate)
        self.detect_hit()
        
    def detect_hit(self):
        for each in self.stored_hor_nums:
            for i in each:
                if self.coordinate == i:
                    print("Hit!")
        for each in self.stored_vert_nums:
            for i in each:
                if self.coordinate == i:
                    print("Hit!!!")

    def create_ships(self):
        self.destroyer = random.randint(1, 2)
        self.submarine = random.randint(1, 2)
        self.cruiser = random.randint(1, 2)
        self.battleship = random.randint(1, 2)
        self.carrier = random.randint(1, 2)

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
board_1.print_board()
board_1.get_ship_location()