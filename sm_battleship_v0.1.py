from random import randint

Board_Shots = []
Board_Boats = []
Boats = []

def calcBoard(Board):
    for n in range(8):
        Board.append(["0"] *8)

def printBoard(PBoard):
    for row in PBoard:
        print(" ".join(row))
#        print(row)

calcBoard(Board_Shots)
calcBoard(Board_Boats)

def random_row(board):
    return randint(0, len(Board_Boats) - 1)

def random_col(board):
    return randint(0, len(Board_Boats[0]) - 1)

def boot_od_wasser(col, row):
    if Board_Boats[row][col] == "B":
        return True
    else:
        return False

def boat(laen):
    ship_row = random_col(Board_Boats)
    print(str(ship_row) + "R")
    ship_col = random_col(Board_Boats)
    print(str(ship_col) + "C")
    ship_dir = randint(0,3)
    print(str(ship_dir) + "D")
    for i in range(laen):
        if ship_dir == 0:
            Board_Boats[ship_row][ship_col] = "B"
            ship_row +=1

        elif ship_dir == 1:
            Board_Boats[ship_row][ship_col] = "B"
            ship_row -= 1

        elif ship_dir == 2:
            Board_Boats[ship_row][ship_col] = "B"
            ship_col += 1

        else:
            Board_Boats[ship_row][ship_col] = "B"
            ship_col -=1
    return


print ("Ende Calcs")
print ("Board_Shots")
printBoard(Board_Shots)

print ("Board_Boats")
printBoard(Board_Boats)
boat(5)
boat(5)
print ("Board_Boats")
printBoard(Board_Boats)
print ("Ende")
