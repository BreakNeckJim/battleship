import random
import math

class Board:
    def __init__(self):
        self.spaces = [*range(1,101)]
        self.board_spaces = {}
        self.stored_vert_nums = []
        self.stored_hor_nums = []
    def __repr__(self):
        return "This is the game board, it contains modules for producing vertical and horizontal pieces, as well as the game board itself!"
    
    def get_vertical(self, size):
        num = random.randint(1, 100)
        print(num)
        stored_vert_nums = []
        stored_vert_nums.append(num)
        if num >= 60:
            stored_vert_nums.append(num-10)
            if size == 2:
                self.stored_vert_nums = stored_vert_nums
                return
            stored_vert_nums.append(num-20)
            if size == 3:
                self.stored_vert_nums = stored_vert_nums
                return
            stored_vert_nums.append(num-30)
            if size == 4:
                self.stored_vert_nums = stored_vert_nums
                return
            stored_vert_nums.append(num-40)
            self.stored_vert_nums = stored_vert_nums
            return  
        else:
            stored_vert_nums.append(num+10)
            if size == 2:
                self.stored_vert_nums = stored_vert_nums
                return
            stored_vert_nums.append(num+20)
            if size == 3:
                self.stored_vert_nums = stored_vert_nums
                return
            stored_vert_nums.append(num+30)
            if size == 4:
                self.stored_vert_nums = stored_vert_nums
                return
            else:
                stored_vert_nums.append(num+40)
                self.stored_vert_nums = stored_vert_nums
                return

    def get_horizontal(self, size):
        num = random.randint(1, 100)
        #print(num)
        #num = 5
        stored_hor_nums = []
        stored_hor_nums.append(num)
        if (num % 10 == 0):
            stored_hor_nums.append(num-1)
            if size == 2:
                self.stored_hor_nums = stored_hor_nums
                return 
            stored_hor_nums.append(num-2)
            if size == 3:
                self.stored_hor_nums = stored_hor_nums
                return 
            stored_hor_nums.append(num-3)
            if size == 4:
                self.stored_hor_nums = stored_hor_nums
                return
            stored_hor_nums.append(num-4)
            self.stored_hor_nums = stored_hor_nums
            return
        elif (num % 10 == 9):
            stored_hor_nums.append(num-1)
            if size == 2:
                self.stored_hor_nums = stored_hor_nums
                return 
            stored_hor_nums.append(num-2)
            if size == 3:
                self.stored_hor_nums = stored_hor_nums
                return 
            stored_hor_nums.append(num-3)
            if size == 4:
                self.stored_hor_nums = stored_hor_nums
                return
            stored_hor_nums.append(num-4)
            self.stored_hor_nums = stored_hor_nums
            return
        elif (num % 10 == 8):
            stored_hor_nums.append(num-1)
            if size == 2:
                self.stored_hor_nums = stored_hor_nums
                return 
            stored_hor_nums.append(num-2)
            if size == 3:
                self.stored_hor_nums = stored_hor_nums
                return 
            stored_hor_nums.append(num-3)
            if size == 4:
                self.stored_hor_nums = stored_hor_nums
                return
            stored_hor_nums.append(num-4)
            self.stored_hor_nums = stored_hor_nums
            return
        elif (num % 10 == 7):
            stored_hor_nums.append(num-1)
            if size == 2:
                self.stored_hor_nums = stored_hor_nums
                return 
            stored_hor_nums.append(num-2)
            if size == 3:
                self.stored_hor_nums = stored_hor_nums
                return 
            stored_hor_nums.append(num-3)
            if size == 4:
                self.stored_hor_nums = stored_hor_nums
                return
            stored_hor_nums.append(num-4)
            self.stored_hor_nums = stored_hor_nums
            return
        elif (num % 10 == 6):
            stored_hor_nums.append(num-1)
            if size == 2:
                self.stored_hor_nums = stored_hor_nums
                return 
            stored_hor_nums.append(num-2)
            if size == 3:
                self.stored_hor_nums = stored_hor_nums
                return 
            stored_hor_nums.append(num-3)
            if size == 4:
                self.stored_hor_nums = stored_hor_nums
                return
            stored_hor_nums.append(num-4)
            self.stored_hor_nums = stored_hor_nums
            return
        else:
            stored_hor_nums.append(num+1)
            if size == 2:
                self.stored_hor_nums = stored_hor_nums
                return 
            stored_hor_nums.append(num+2)
            if size == 3:
                self.stored_hor_nums = stored_hor_nums
                return 
            stored_hor_nums.append(num+3)
            if size == 4:
                self.stored_hor_nums = stored_hor_nums
                return
            stored_hor_nums.append(num+4)
            self.stored_hor_nums = stored_hor_nums
            return


board_1 = Board()
board_1.get_vertical(5)
board_1.get_horizontal(4)
print(board_1.stored_hor_nums)
print(board_1.stored_vert_nums)
