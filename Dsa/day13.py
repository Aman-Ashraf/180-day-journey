#  def reverse(str):
#     if str == str[-1]:
#         return str

#     return reverse(str[1:])+ str[0]
# print(reverse ("DOG"))

# def pal(str): 
#     if str[0] == str[-1]:
#         return pal(str[1:-1])
# print(reverse ("DOG"))

# def palindrome(str):
#     if len(str) <= 1:
#         return True

#     if str[0] != str[-1]:
#         return False

#     return palindrome(str[1:-1])
# print(palindrome("MAM"))

# def list_sum(nums):
#     if len(nums) <= 1:
#         return nums[0]
#     return nums[0] + list_sum(nums[1:]) 
# print(list_sum([10,20,30,40]))


# def find_max(nums):
#     if len(nums) == 1:
#         return nums[0]
#     if nums == nums[-1]:
#         return 
#     return find_max(nums[1:])


def find_max(nums):
    if len(nums) == 1:
        return nums[0]
    
    rest_max = find_max(nums[1:])
    if nums[0] > rest_max:
        return nums[0]

    return rest_max

print(find_max([8, 3, 15, 6, 12]))
