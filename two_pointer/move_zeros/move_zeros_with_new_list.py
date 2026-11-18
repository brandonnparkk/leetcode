def move_zeroes(nums: list[int]) -> list[int]:
    pass
    result = [num for num in nums if num!= 0]
    result += [0] * (len(nums) - len(result))
    nums[:] = result
    return nums