def solve(index, current, total):

    if total == target:
        print(current)
        return

    if total > target:
        return

    if index == len(candidates):
        return

    # Take
    current.append(candidates[index])
    solve(index, current, total + candidates[index])
    current.pop()

    # Skip
    solve(index + 1, current, total)

candidates = [2, 3]
target = 6
solve(0, [], 0)