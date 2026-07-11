numbers = [7, 2, 15, 8, 3]

# for number in numbers:
#     if number % 2 != 0:
#         print (number ,end=" ")

largest = float('-inf')
second_largest = float('-inf')

for number in numbers:
    if largest < number:
        second_largest = largest
        largest = number
        
    if second_largest < number < largest:
        second_largest = number

print(largest, second_largest)