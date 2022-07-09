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
    
    def get_vertical_3(self):
        num = random.randint(1, 100)
        stored_vert_nums = []
        stored_vert_nums.append(num)
        if (num+10) < 100:
            stored_vert_nums.append(num+10)
            num = num+10
        else:
            stored_vert_nums.append(num-10)
            stored_vert_nums.append(num-20)
            self.stored_vert_nums = stored_vert_nums
            return
        if (num+10) < 100:
            stored_vert_nums.append(num+10)
        else:
            stored_vert_nums.append(num-20)
        self.stored_vert_nums = stored_vert_nums

    def get_horizontal_3(self):
        num = random.randint(1, 100)
        #num = 5
        stored_hor_nums = []
        stored_hor_nums.append(num)
        if (num % 10 == 0):
            stored_hor_nums.append(num-1)
            stored_hor_nums.append(num-2)
            self.stored_hor_nums = stored_hor_nums
            return
        elif (num % 10 == 9):
            stored_hor_nums.append(num-1)
            stored_hor_nums.append(num-2)
            self.stored_hor_nums = stored_hor_nums
        else:
            stored_hor_nums.append(num+1)
            stored_hor_nums.append(num+2)
            self.stored_hor_nums = stored_hor_nums
board_1 = Board()
board_1.get_vertical_3()
board_1.get_horizontal_3()
print(board_1.stored_hor_nums)
