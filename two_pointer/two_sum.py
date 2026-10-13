class Solution:
    def twoSum(self, nums: List[int], target: int) -> bool:
        # Your code goes here
        lp, rp = 0, len(nums) - 1
        while lp < rp:
            curr_sum = nums[lp] + nums[rp]
            if curr_sum == target:
                return True
            if curr_sum < target:
                lp += 1
            else:
                rp -= 1
        
        return False