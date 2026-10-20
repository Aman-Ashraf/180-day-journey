#🚀 Day 38 — Split Array Largest Sum (LeetCode #410)

def splitArraySum(nums, k):
    left = max(nums)
    right = sum(nums)

    while left < right:
        mid = (left + right) // 2
        groups = 1
        current_sum = 0

        for num in nums:
            if current_sum + num <= mid:
                current_sum += num
            else:
                groups += 1
                current_sum = num

        if groups <= k:
            right = mid
        else:
            left = mid + 1  
    return left

nums = [7, 2, 5, 10, 8]
k = 2
print(splitArraySum(nums, k))