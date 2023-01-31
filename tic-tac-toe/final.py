grid = [" " for m in range(0, 9)]
gridlist = list(map(str, grid))


def printgrid():
    print(f'''---------
| {grid[0]} {grid[1]} {grid[2]} |
| {grid[3]} {grid[4]} {grid[5]} |
| {grid[6]} {grid[7]} {grid[8]} |
---------''')


def check(c1, c2, c3):
    if c1 == c2 and c2 == c3 and c1 != ' ' and c2 != ' ' and c3 != ' ':
        return True
    else:
        return False


def checkwin():
    # Horizontal checks
    if check(grid[0], grid[1], grid[2]) is True or check(
            grid[3], grid[4], grid[5]) is True or check(
                grid[6], grid[7], grid[8]) is True:
        print(f"{turn} wins")
        exit()
    # Vertical checks
    if check(grid[0], grid[3], grid[6]) is True or check(
            grid[1], grid[4], grid[7]) is True or check(
                grid[2], grid[5], grid[8]) is True:
        print(f"{turn} wins")
        exit()
    # Diagonal checks
    if check(grid[0], grid[4], grid[8]) is True or check(
            grid[2], grid[4], grid[6]) is True:
        print(f"{turn} wins")
        exit()


x = 0
turn = "X"


class LengthError(Exception):
    pass


class SizeError(Exception):
    pass


class PlaceError(Exception):
    pass


print(
    "Hello! Please enter the row and column where you would like to place your marker! E.g. '1 1' to place your marker in the top left corner."
)
printgrid()
while x < 9:
    num = input("Enter the coordinates: ")
    place = num.split()
    try:
        coordinates = [int(s) for s in place]
        if len(coordinates) > 2 or len(coordinates) < 2:
            raise LengthError()
        elif coordinates[0] > 3 or coordinates[0] < 0 or coordinates[
                1] > 3 or coordinates[1] < 0:
            raise SizeError()
        else:
            i = (((coordinates[0] - 1) * 3) + (coordinates[1] + 2)) - 3
            if gridlist[i] == "X" or gridlist[i] == "O":
                raise PlaceError()
    except TypeError:
        print("You should enter numbers!")
    except LengthError:
        print("You should enter numbers!")
    except SizeError:
        print("Coordinates should be from 1 to 3!")
    except PlaceError:
        print("This cell is occupied! Choose another one!")
    else:
        gridlist[i] = turn
        grid = ''.join(gridlist)
        printgrid()
        checkwin()

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        x = x + 1

if x == 9:
    print("Draw")
