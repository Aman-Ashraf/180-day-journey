def bubble_sort(nums, n):

    if n == 1:
        return
    for i in range (n-1):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1],nums[i]

    return bubble_sort(nums, n-1)
nums = [5, 3, 4, 1]
bubble_sort(nums, len(nums))

print(nums)
