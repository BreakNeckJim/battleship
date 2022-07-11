import random

board = []
spaces = []
ship_coordinates = []
correct_guesses = []
coordinate = 0
letters_to_numbers = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9}

def get_ship_location():
    global turns
    row = input("Please enter a row 1-10 ")
    while row not in "123456789 10":
        print("Please enter a valid row ")
        row = input("Please enter a row 1-10 ")
    column = input("Please enter a column A-J ").upper()
    while column not in "ABCDEFGHIJ":
        print("Please enter a valid column ")
        column = input("Please enter a column A-J ").upper()
    coordinate = (int(row)-1)*10 + int(letters_to_numbers[column]+1)
    row = int(row) - 1
    print(coordinate)
    for each in ship_coordinates:
        if coordinate == each:
            board[int(row)][int(letters_to_numbers[column])] = "X"
            print(ship_coordinates)
            correct_guesses.append(each)
            ship_coordinates.pop(ship_coordinates.index(each))
            print(ship_coordinates)
            print(correct_guesses)
            print("Hit!")
            break
        else:
            board[int(row)][int(letters_to_numbers[column])] = "/"
            print("Sorry, guess again!")
            turns -= 1


def create_ships():
    destroyer = random.randint(1, 2)
    submarine = random.randint(1, 2)
    cruiser = random.randint(1, 2)
    battleship = random.randint(1, 2)
    carrier = random.randint(1, 2)
    if destroyer == 1:
        get_vertical(2)
    else:
        get_horizontal(2)
    
    if submarine == 1:
        get_vertical(3)
    else:
        get_horizontal(3)
    
    if cruiser == 1:
        get_vertical(3)
    else:
        get_horizontal(3)
    
    if battleship == 1:
        get_vertical(4)
    else:
        get_horizontal(4)
    
    if carrier == 1:
        get_vertical(5)
    else:
        get_horizontal(5)

def get_vertical(size):
    num = random.randint(1, 100)
    global ship_coordinates
    correct_coordinates = []
    correct_coordinates.append(num)
    if num >= 60:
        correct_coordinates.append(num-10)
        if size == 2:
            ship_coordinates += correct_coordinates
            return
        correct_coordinates.append(num-20)
        if size == 3:
            ship_coordinates += correct_coordinates
            return
        correct_coordinates.append(num-30)
        if size == 4:
            ship_coordinates += correct_coordinates
            return
        correct_coordinates.append(num-40)
        ship_coordinates += correct_coordinates
        return  
    else:
        correct_coordinates.append(num+10)
        if size == 2:
            ship_coordinates += correct_coordinates
            return
        correct_coordinates.append(num+20)
        if size == 3:
            ship_coordinates += correct_coordinates
            return
        correct_coordinates.append(num+30)
        if size == 4:
            ship_coordinates += correct_coordinates
            return
        else:
            correct_coordinates.append(num+40)
            ship_coordinates += correct_coordinates
            return

def get_horizontal(size):
    num = random.randint(1, 100)
    correct_coordinates = []
    global ship_coordinates
    correct_coordinates.append(num)
    if (num % 10 == 0) or (num % 10 == 9) or (num % 10 == 8) or (num % 10 == 7) or (num % 10 == 6):
        correct_coordinates.append(num-1)
        if size == 2:
            ship_coordinates += correct_coordinates
            return 
        correct_coordinates.append(num-2)
        if size == 3:
            ship_coordinates += correct_coordinates
            return 
        correct_coordinates.append(num-3)
        if size == 4:
            ship_coordinates += correct_coordinates
            return
        correct_coordinates.append(num-4)
        ship_coordinates += correct_coordinates
        return
    else:
        correct_coordinates.append(num+1)
        if size == 2:
            ship_coordinates += correct_coordinates
            return 
        correct_coordinates.append(num+2)
        if size == 3:
            ship_coordinates += correct_coordinates
            return 
        correct_coordinates.append(num+3)
        if size == 4:
            ship_coordinates += correct_coordinates
            return
        correct_coordinates.append(num+4)
        ship_coordinates += correct_coordinates
        return

for i in range(0, 10):
    board.append(["O"] * 10)

def print_board(board):
    print("  A B C D E F G H I J")
    x = 1
    for i in board:
        print(str(x) + " " + " ".join(i))
        x += 1

turns = 20
print(turns)
while turns > 0:
    print_board(board)
    create_ships()
    print(ship_coordinates)
    get_ship_location()
    print_board(board)
    print(turns)