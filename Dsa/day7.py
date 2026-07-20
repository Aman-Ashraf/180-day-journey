# git@github.com:Aman-Ashraf/180-day-journey.git

rows = 5

# for row in range (1,rows + 1 ):

#     for space in range(rows - row):
#         print(" ", end="")

#     for inc in range (row):
#         print(inc + 1 , end="")

#     for dec in range(row -1, 0, -1):
#         print(dec , end="")
    
#     print()

for row in range (5,5 - rows , -1 ):
    for space in range(rows - row):
        print(" ", end="")

    for inc in range (row):
        print(inc + 1 , end="")

    for dec in range(row -1, 0, -1):
        print(dec , end="")
    
    print()