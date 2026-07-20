
# def largestno(numbers):

#     largest = float("-inf")

#     for number in numbers:
#         if number > largest:
#             largest = number
#     return largest

# print(largestno([12,4,5,7,34,32]))

# def Evenno(numbers):
#     count = 0
#     for number in numbers:
#         if number % 2 == 0:
#             count += 1
#     return count
    
# nums = [7, 2, 15, 8, 3, 10]

# no = Evenno(nums)
# print(no)

# def search(num,target):

#     found = False
    
#     for number in num:
#         if number  == target:
#             found = True
#             break
#     return found
# # # or 
# def search(num, target):
#     for number in num:
#         if number == target:
#             return True

#     return False
    
# nums = [7, 2, 15, 8, 3, 10]
# print(search(nums, 8))

def second_largest(numbers):
    largest = float('-inf')
    second_largest = float('-inf')
    for num in numbers:
        if  num > largest :
            second_largest=largest
            largest = num
            continue
        elif largest > num > second_largest:
            second_largest = num
    return largest, second_largest

nums = [7, 2, 15, 8, 3]

print(second_largest(nums))