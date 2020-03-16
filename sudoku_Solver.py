# -- Santiago Caro Duque


def read_game(file_name):
    f = open(file_name, 'r')
    game = [[None for y in range(9)] for x in range(9)]
    for i in range(9):
        game[i] = f.readline().split()
    return game


def get_posibilities(game, row, column):
    posibilities = []
    negative = []
    for i in range(9):
        posibilities.append(str(i+1))
    for i in range(9):
        if not game[row][i] in negative:
            negative.append(game[row][i])
    for j in range(9):
        if not game[j][column] in negative:
            negative.append(game[j][column])
    quadrant_negative = get_quadrant_possibilities(game, row, column)

    posibilities = list(set(posibilities)-set(negative))
    posibilities = list(set(posibilities) - set(quadrant_negative))
    return posibilities


def get_quadrant_possibilities(game, row, column):
    quadrant_row = int(int(row)/3)
    quadrant_column = int(int(column)/3)
    negative = []
    rows = quadrant_row*3
    colums = quadrant_column*3
    for i in range(rows, rows+3):
        for j in range(colums, colums+3):
            if not game[i][j] in negative:
                negative.append(game[i][j])
    return negative


def done(game):
    for i in range(9):
        for j in range(9):
            if game[i][j] == '0':
                return False
    return True


def solve_game(game):
    if done(game):
        return True
    else:
        for row in range(9):
            for column in range(9):
                if game[row][column] == '0':
                    posibilities = get_posibilities(game, row, column)
                    if len(posibilities) == 0:
                        return False
                    else:
                        for k in posibilities:
                            game[row][column] = k
                            if solve_game(game):
                                return True
                            game[row][column] = '0'
                        return False


game = read_game("Extreme.txt")
print(solve_game(game))


for i in game:
    print(*i, sep=" ")
