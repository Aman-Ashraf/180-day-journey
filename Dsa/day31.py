#insert position of target in a sorted array
def insert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:

        mid = (left + right)//2

        if nums[mid] == target:
            return mid
        
        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return left

nums = [-1,0,3,4,5,6,7,8,9,10]
target = 12
print(insert(nums, target))
