#875 Koko Eating Bananas
def minEatingSpeed(piles, h):
    left = 1
    right = max(piles)
    while left < right:
        mid = (left + right) // 2
        hours = 0
        for pile in piles:
            hours += (piles + mid - 1)
        if hours < h:
            right = mid
        else:
            left = mid + 1
    return left

piles = [5, 8, 10]
h = 6
print(minEatingSpeed(piles, h))