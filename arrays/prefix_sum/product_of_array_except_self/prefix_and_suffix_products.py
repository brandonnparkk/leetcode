def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    answer = [i] * n
    prefix = 1

    for i in range(n):
        # product of nums[:i]
        answer[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n -1, -1, -1):
        # times product of nums[i + 1:]
        answer[i] *= suffix
        suffix *= nums[i]

    return answer