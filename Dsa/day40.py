#Day 40 — Search a 2D Matrix II (LeetCode #240)
def searchMatrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])

    row = 0
    col = cols - 1
    while row < rows and col >= 0:
        current = matrix[row][col]
        if current == target:
            return True
        elif current > target:
            col -= 1
        else:
            row += 1
    return False

matrix = [
    [1,  4,  7, 11, 15],
    [2,  5,  8, 12, 19],
    [3,  6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

print(searchMatrix(matrix, 5))   # True
print(searchMatrix(matrix, 20))  # False
print(searchMatrix(matrix, 16))  # True