def product_except_self(nums: list[int]) -> list[int]:
    answer = []
    for i in range(len(nums)):
        product = 1
        for j, num in enumerate(nums):
            if j != i:
                product *= num
        answer.append(product)

    return answer