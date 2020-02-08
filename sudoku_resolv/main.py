from os import system

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


# function to print the board
def print_board(bo):
    print("*********************")
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(str(bo[i][j]))
            else:
                print(str(bo[i][j]) + " ", end="")
    print("*********************")


# function to retrieve case with 0
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j  # row, column


# validate a value
def valid(bo, num, pos):
    # check value on the same row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num:
            return False

    # check value on the same column
    for i in range(len(bo[0])):
        if bo[i][pos[1]] == num:
            return False

    # check value on the same sub square
    x = pos[0] // 3
    y = pos[1] // 3

    for i in range(len(bo[0])):
        for j in range(len(bo[0])):
            if i // 3 == x and j // 3 == y:
                if bo[i][j] == num:
                    return False
    return True


def fill_empty(bo):
    if not find_empty(bo):
        return True
    else:
        pos = find_empty(bo)
        for index in range(1, 10):
            if valid(bo, index, pos):
                bo[pos[0]][pos[1]] = index

                if fill_empty(bo):
                    return True

            bo[pos[0]][pos[1]] = 0
    return False


if __name__ == '__main__':
    print_board(board)
    fill_empty(board)
    print_board(board)
