# Combination Sum II
def solve(index, current, total):
    if total == target:
        result.append(current.copy())
        return

    if total > target:
        return

    if index == len(candidates):
        return

    for i in range(index, len(candidates)):
        if i > index and candidates[i] == candidates[i - 1]:
            continue

        current.append(candidates[i])

        solve(i + 1, current, total + candidates[i])

        current.pop()

candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
result=[]
candidates.sort()
solve(0, [], 0)

print(result)