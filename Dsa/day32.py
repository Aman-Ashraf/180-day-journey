def findFirst(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right :
        mid = (left + right) // 2
        if nums[mid] == target:
            answer = mid 
            right = mid - 1
        elif nums[mid] < target :
            left = mid + 1
        else:
            right = mid - 1
    return answer

def findLast(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right :
        mid = (left + right) // 2
        if nums[mid] == target:
            answer = mid 
            left = mid + 1
        elif nums[mid] < target :
            left = mid + 1
        else:
            right = mid - 1
    return answer


nums = [5, 7, 7, 8, 8, 10]
target = 8
answer = -1

print(findFirst(nums,target),findLast(nums,target))