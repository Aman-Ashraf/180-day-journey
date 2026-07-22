def bubble_sort(nums, n):

    if n == 1:
        return 

    # One Bubble Sort pass happens here

    return bubble_sort(nums, n-1)
print (bubble_sort(5,4))