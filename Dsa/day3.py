numbers = [7, 2, 15, 8, 3]

# found = False

# for number in numbers:
#     if number == 8:
#         found = True
# if found ==False:
#     print("8 not found")
# else:
#     print("8 found")

# start = 0
# for number in numbers:
#     if number == 8:
#         print("Index :", start)
#         break
#     start += 1

for number in numbers:
    if number % 2 != 0:
        continue
    print("Even numbers :" , number)