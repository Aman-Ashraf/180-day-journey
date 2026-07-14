numbers = [1, 2, 2, 3, 2, 4, 1]

# count = 0

# for number in numbers:
#     if number == 2:
#         count += 1

# print("2 appears :", count, "times")

freq = {}

for number in numbers:
    if number in freq:
        freq[number] += 1
    else:
        freq[number] = 1

print("frequencies : ",freq)

