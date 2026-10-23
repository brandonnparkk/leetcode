def triangleNumber(self, nums: List[int]) -> int:
    nums.sort()
    count = 0
    for i in range(len(nums) - 1, 1, -1):
        lp = 0
        rp = i - 1
        while lp < rp:
            if nums[lp] + nums[rp] > nums[i]:
                count += rp - lp
                rp -= 1
            else:
                lp += 1
    return count