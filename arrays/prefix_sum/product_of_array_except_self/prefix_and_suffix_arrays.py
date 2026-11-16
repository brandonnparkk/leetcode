def product_except_self(nums: list[int]) -> list[int]:
    # Input: nums = [1,2,3,4]
    # Output: [24,12,8,6]

    # it's asking nums[i] is the product of everything left of it * everything right of it
    # the key is to precomute both in two arrays

    # approach:
    # 1. build prefix[i], the product of nums[:i]
    # 2. build suffix[i], the product of nums[i + 1:]
    # 3. return the prefix[i] * suffix[i] for every i

    n = len(nums)
    prefix = [1] * n
    suffix = [1] * n

    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]

    return [prefix[i] * suffix[i] for i in range(n)]

    