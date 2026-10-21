#Day 39 — Search a 2D Matrix (LeetCode #74)

def matrixSearch(matrix, target):
    rows = len(matrix)
    columns = len(matrix[0])

    left = 0
    right = rows * columns - 1

    while left <= right:
        mid = (left + right) // 2

        rows = mid // columns
        col = mid % columns
        if matrix[rows][col] == target:
            return True
        elif matrix[rows][col] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

matrix = [
    [1,  3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 1
print(matrixSearch(matrix, target))