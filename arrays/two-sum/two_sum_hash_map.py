def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        # looks for the complement
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
