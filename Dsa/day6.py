rows = 5

# for row in range(1, rows +1):
#     for col in range(row):
#         print("*", end="")
#     print()

# for row in range(1, rows +1):
#     for col in range(rows - row ):
#         print(" ", end="")
#     print("*"*(row))

# rows = 5

# for row in range(1, rows + 1):

#     # Print spaces
#     for space in range(rows - row):
#         print(" ", end="")

#     # Print stars
#     for star in range(row):
#         print("*", end="")

#     # Move to the next line
#     print()


# for row in range(1,rows + 1):
#     for col in range(1, row +1):
#         print(col, end="")
#     print()

# for row in range(1,rows + 1):
#     for col in range(5, 5-row, -1):
#         print(col, end="")
#     print()

for row in range (1,rows + 1 ):
    for col in range (row):
        print(row, end="")
    print()
