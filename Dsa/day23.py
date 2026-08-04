#letter combinations

def solve(index, current):

    if index == len(digits):
        result.append(current)
        return

    for letter in phone[digits[index]]:

        current += letter

        solve(index + 1, current)

        current = current[:-1]

result = []
digits = "23"

phone = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}


solve(0, "")
print(result)