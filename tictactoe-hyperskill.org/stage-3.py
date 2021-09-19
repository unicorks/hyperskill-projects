grid = input("Enter cells: ")

print("---------")
print(f'| {grid[0]} {grid[1]} {grid[2]} |')
print(f'| {grid[3]} {grid[4]} {grid[5]} |')
print(f'| {grid[6]} {grid[7]} {grid[8]} |')
print("---------")


def check(c1, c2, c3):
    if c1 == c2 and c2 == c3 and c1 != '_':
        return True
    else:
        return False


def convert(string):
    list1 = []
    list1[:0] = string
    return list1


wins = 0

# Horizontal checks
if check(grid[0], grid[1], grid[2]) is True:
    wins = wins + 1
    winner = grid[0]
if check(grid[3], grid[4], grid[5]) is True:
    wins = wins + 1
    winner = grid[3]
if check(grid[6], grid[7], grid[8]) is True:
    wins = wins + 1
    winner = grid[6]

# Vertical checks
if check(grid[0], grid[3], grid[6]) is True:
    wins = wins + 1
    winner = grid[0]
if check(grid[1], grid[4], grid[7]) is True:
    wins = wins + 1
    winner = grid[1]
if check(grid[2], grid[5], grid[8]) is True:
    wins = wins + 1
    winner = grid[2]

# Diagonal checks
if check(grid[0], grid[4], grid[8]) is True:
    wins = wins + 1
    winner = grid[0]
if check(grid[2], grid[4], grid[6]) is True:
    wins = wins + 1
    winner = grid[2]

# print winner
if wins == 1:
    # noinspection PyUnboundLocalVariable
    print(f"{winner} wins")
    exit()

# print draw
if wins == 0 and '_' not in grid:
    print("Draw")
    exit()

grid_list = convert(grid)
x_count = grid_list.count('X')
o_count = grid_list.count('O')

if wins > 1 or x_count - o_count > 1 or o_count - x_count > 1:
    print("Impossible")
    exit()

blanks = grid_list.count('_')

if wins == 0 and blanks > 0:
    print("Game not finished")
    exit()
