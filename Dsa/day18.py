#subsets

def solve(index, current):
    #Base case
    if index == len(nums):
        print(current)
        return

    #take
    current.append(nums[index])
    solve(index+1,current)
    current.pop()
    #skip
    solve(index+1, current)

nums = [1, 2]

solve(0, [])