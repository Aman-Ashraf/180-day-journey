def solve(current):

    # Base case
    if len(current) == 2:
        print(current)
        return

    # Generate choices
    for choice in ["0", "1"]:

        # Choose
        current = current + choice

        # Explore
        solve(current)

        # Undo
        current = current[:-1]

solve("")

#generate strings