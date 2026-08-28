# LeetCode 51: N-Queens

n = 4

board = [["." for _ in range(n)] for _ in range(n)]

result = []


def isSafe(row, col):

    # Check same column
    r = row - 1

    while r >= 0:
        if board[r][col] == "Q":
            return False

        r -= 1

    # Check upper-left diagonal
    r = row - 1
    c = col - 1

    while r >= 0 and c >= 0:
        if board[r][c] == "Q":
            return False

        r -= 1
        c -= 1

    # Check upper-right diagonal
    r = row - 1
    c = col + 1

    while r >= 0 and c < n:
        if board[r][c] == "Q":
            return False

        r -= 1
        c += 1

    return True


def solve(row):

    # All queens placed
    if row == n:
        result.append(["".join(r) for r in board])
        return

    # Try every column
    for col in range(n):

        # Check whether position is safe
        if isSafe(row, col):

            # Choose
            board[row][col] = "Q"

            # Explore
            solve(row + 1)

            # Undo
            board[row][col] = "."


solve(0)

print(result)