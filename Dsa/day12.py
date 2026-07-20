# def factorial(n):
#     if n == 0:
#         return 1

#     return n * factorial(n - 1)

# print(factorial(4))

# def sum_n(n):
#     if n == 0 :
#         return 0
#     return n + sum_n(n - 1)

# print(sum_n(5))

def pow(n , p):
    if p == 0:
        return 1
    return n * pow(n , p - 1)

print(pow(5, 3))