def two_sum(nums: list[int], target: int) -> list[int]:
    # Write your solution here
    pass
    indexes = sorted(range(len(nums)), key=lambda i: nums[i])
    lp, rp = 0, len(nums) - 1
    while lp < rp:
        sum = nums[indexes[lp]] + nums[indexes[rp]]
        if sum == target:
            return indexes[lp], indexes[rp]
        elif sum <= target:
            lp += 1
        else:
            rp -= 1
    