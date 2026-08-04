def isPalindrome(string):
    return string == string[::-1]

def solve(index, current):

    if index == len(s):
        print(current)
        return

    for end in range(index, len(s)):

        substring = s[index:end+1]

        if isPalindrome(substring):

            current.append(substring)

            solve(end + 1, current)

            current.pop()

s = "banana"
index = 0
current = []

solve(0, [])