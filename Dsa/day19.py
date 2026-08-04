def solve( current):
    if len(current) == len(nums):
        print (current)
        return
    for num in nums:
        if num in current:
            continue

        current.append(num)

        solve(current)

        current.pop()

nums = [1, 2]
solve([])