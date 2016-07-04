from random import randint

Board_Shots = []
Board_Boats = []
Boats = []

def calcBoard(Board):
    for n in range(9):
        Board.append(["O"] *9)

def printBoard(PBoard):
    for row in PBoard:
        print(" ".join(row))

def boot_od_wasser(col, row):
    if Board_Boats[row][col] == "B":
        return True
    else:
        return False

def boat(laen):
    ship_row = 0
    ship_col = 0
    ship_dir = randint(0,3)
    if ship_dir == 0:
        ship_row = randint(1,(8-laen))
        ship_col = randint(1,8)
        for i in range(laen):
            Board_Boats[ship_row][ship_col] = "B"
            ship_row +=1

    elif ship_dir == 1:
        ship_row = randint((1+laen),8)
        ship_col = randint(1,8)
        for i in range(laen):
            Board_Boats[ship_row][ship_col] = "B"
            ship_row -= 1

    elif ship_dir == 2:
        ship_row = randint(1,8)
        ship_col = randint(1,(8-laen))
        for i in range(laen):
            Board_Boats[ship_row][ship_col] = "B"
            ship_col += 1

    elif ship_dir == 3:
        ship_row = randint(1,8)
        ship_col = randint((1+laen),8)
        for i in range(laen):
            Board_Boats[ship_row][ship_col] = "B"
            ship_col -=1
    else:
        print("Error def Boat()")

def boote_berechnen():
    for i in range(4):
        boat(2)
    for i in range(3):
        boat(3)
    for i in range(2):
        boat(4)
    boat(5)


def treffer_berechen():
    tre_min = 0
    for i in range(len(Board_Boats)):
        for d in range(len(Board_Boats[0])):
            if Board_Boats[i][d] == "B":
                tre_min += 1
    return tre_min

def numbers(Board):
    for i in range(len(Board)):
        Board[i][0] = str(i)
    for i in range(len(Board[0])):
        Board[0][i] = str(i)


calcBoard(Board_Shots)
calcBoard(Board_Boats)
numbers(Board_Boats)
numbers(Board_Shots)
boote_berechnen()
treffer_min = treffer_berechen()
print ("Game Start")
print("Min Shots " + str(treffer_min))
printBoard(Board_Shots)

trys = 0
treffer = 0
while True:
    print("Shots fired " + str(trys))
    print("Hit Nr." + str(treffer))
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))
    trys += 1

    if guess_row < 1 or guess_col < 1 or guess_row > 8 or guess_col > 8:
        print("Out Of Range")
    else:
        if Board_Shots[guess_row][guess_col] == "X" or Board_Shots[guess_row][guess_col] == "M":
            print("Dubble")
        elif Board_Boats[guess_row][guess_col] == "B":
            Board_Shots[guess_row][guess_col] = "X"
            treffer += 1
            print("Hit Nr." + str(treffer))
            print("Nice Shot")
            if treffer == treffer_min:
                break
        else:
            print("Missed")
            Board_Shots[guess_row][guess_col] = "M"
    printBoard(Board_Shots)

print("Winner in" + str(trys) + " Shots")
print ("All the Boats")
printBoard(Board_Boats)

print ("Thanks play again!")
