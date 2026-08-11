#word search
board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]

word = "ABCCED"


def dfs(row, col, index):

    if index == len(word):
        return True

    if row < 0 or row >= len(board):
        return False

    if col < 0 or col >= len(board[0]):
        return False

    if board[row][col] == "#" or board[row][col] != word[index]:
        return False

    temp = board[row][col]
    board[row][col] = "#"

    found = (
        dfs(row + 1, col, index + 1) or
        dfs(row - 1, col, index + 1) or
        dfs(row, col + 1, index + 1) or
        dfs(row, col - 1, index + 1)
    )

    board[row][col] = temp

    return found


def exist():

    for row in range(len(board)):
        for col in range(len(board[0])):

            if dfs(row, col, 0):
                return True

    return False


print(exist())
