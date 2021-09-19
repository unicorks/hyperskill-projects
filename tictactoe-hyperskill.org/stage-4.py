grid1 = input("Enter cells: ")
grid = grid1.replace("_", " ")
gridlist = list(map(str, grid))

print("---------")
print(f'| {grid[0]} {grid[1]} {grid[2]} |')
print(f'| {grid[3]} {grid[4]} {grid[5]} |')
print(f'| {grid[6]} {grid[7]} {grid[8]} |')
print("---------")

x = 0


class LengthError(Exception):
    pass


class SizeError(Exception):
    pass


class PlaceError(Exception):
    pass


while x < 5:
    num = input("Enter the coordinates: ")
    place = num.split()
    try:
        coordinates = [int(s) for s in place]
        if len(coordinates) > 2 or len(coordinates) < 2:
            raise LengthError()
        elif coordinates[0] > 3 or coordinates[0] < 0 or coordinates[1] > 3 or coordinates[1] < 0:
            raise SizeError()
        else:
            i = (((coordinates[0] - 1) * 3) + (coordinates[1] + 2)) - 3
            if gridlist[i] == "X" or gridlist[i] == "O":
                raise PlaceError()
    except LengthError:
        print("You should enter numbers!")
    except SizeError:
        print("Coordinates should be from 1 to 3!")
    except PlaceError:
        print("This cell is occupied! Choose another one!")
    else:
        gridlist[i] = "X"
        grid = ''.join(gridlist)
        print("---------")
        print(f'| {grid[0]} {grid[1]} {grid[2]} |')
        print(f'| {grid[3]} {grid[4]} {grid[5]} |')
        print(f'| {grid[6]} {grid[7]} {grid[8]} |')
        print("---------")
        break
