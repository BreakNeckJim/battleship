import random
import math

class Board:
    def __init__(self):
        self.spaces = [*range(1,101)]
        self.board_spaces = {}
        self.stored_vert_nums = []
    def __repr__(self):
        return "This is the game board, it contains modules for producing vertical and horizontal pieces, as well as the game board itself!"
    def get_vertical(self):
        num = random.randint(1, 100)
        print(num)
        stored_vert_nums = []
        print(stored_vert_nums)
        stored_vert_nums.append(num)
        if (num+10) < 100:
            stored_vert_nums.append(num+10)
            print(stored_vert_nums)
        else:
            stored_vert_nums.append(num-10)
            print(stored_vert_nums)
        if (num+20) < 100:
            stored_vert_nums.append(num+20)
            print(stored_vert_nums)
        else:
            stored_vert_nums.append(num-20)
            print(stored_vert_nums)
        self.stored_vert_nums = stored_vert_nums
board_1 = Board()
board_1.get_vertical()
print(board_1.stored_vert_nums)
