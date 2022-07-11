import random

board = []
spaces = []
ship_coordinates = []
correct_guesses = []
coordinate = 0
letters_to_numbers = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9}
turns = 20

def get_ship_location():
    global turns
    row = input("\nPlease enter a row 1-10 ")
    while row not in "123456789 10":
        print("\nPlease enter a valid row ")
        row = input("\nPlease enter a row 1-10 ")
    column = input("\nPlease enter a column A-J ").upper()
    while column not in "ABCDEFGHIJ":
        print("\nPlease enter a valid column ")
        column = input("\nPlease enter a column A-J ").upper()
    coordinate = (int(row)-1)*10 + int(letters_to_numbers[column]+1)
    row = int(row) - 1

    if coordinate in ship_coordinates:
        board[int(row)][int(letters_to_numbers[column])] = "X"
        correct_guesses.append(coordinate)
        ship_coordinates.pop(ship_coordinates.index(coordinate))
        print("Hit!\n")
    else:
        board[int(row)][int(letters_to_numbers[column])] = "/"
        turns -= 1
        print("\n\nSorry, guess again!\n")
        

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
        print("  " + " ".join(i) + " " + str(x))
        x += 1

create_ships()

print("\nHello and welcome to battleship!\n")
print("You have " + str(turns) + " turns left\n")

while turns > 0 and len(correct_guesses) < 17:
    print_board(board)
    get_ship_location()
    print("You have " + str(turns) + " turns left\n")

if turns == 0:
    print("Sorry, you've run out of turns!\nThanks for playing!")

if len(correct_guesses) == 17:
    print("Congratulations!!! You've sunk all the ships!\nYou win!")