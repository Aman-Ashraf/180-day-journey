#Day 37 — Binary Search on Answer 🔥 Day 37 🚀 — Capacity To Ship Packages Within D Days (#1011)

def shipWithinDays(weights, days):
    left = max(weights)
    right = sum(weights)

    while left < right:
        mid = (left + right) // 2

        # Count the days needed for this capacity
        current_load = 0
        days_needed = 1

        for weight in weights:
            if current_load + weight <= mid:
                current_load += weight
            else:
                days_needed += 1
                current_load = weight

        # Decide which half to search
        if days_needed <= days:
            right = mid
        else:
            left = mid + 1

    return left

weights = [7, 2, 5, 3]
days = 3
print(shipWithinDays(weights, days))