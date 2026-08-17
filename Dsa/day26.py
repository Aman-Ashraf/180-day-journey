# Grnerate parenthesis
def solve(open, close, current):
    if len(current) == 2 * n:
        result.append(current)
        return

    if open < n:

        current += "("

        solve(open + 1, close, current)

        current = current[:-1]

    if close < open:

        current += ")"

        solve(open, close + 1, current)

        current = current[:-1]

n = 3
result = []
solve(0, 0, "")
print(result)