# def binary_search(nums, left, right, target):
#     if left > right:
#         return -1
#     mid = (left + right) // 2
#     if nums[mid] == target:
#         return mid
#     if target < nums[mid]:
#         return binary_search(nums, left, mid - 1, target)
    
#     return binary_search(nums, mid + 1, right, target)
# print(binary_search([1,2,3,4,5],0,4,2))

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(4))

