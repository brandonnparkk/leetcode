class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Your code goes here
        nums.sort()
        output = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lp, rp = i + 1, len(nums) - 1
            while lp < rp:
                curr_sum = nums[i] + nums[lp] + nums[rp]
                if curr_sum < 0:
                    lp += 1
                elif curr_sum > 0:
                    rp -= 1
                else:
                    output.append([nums[i], nums[lp], nums[rp]])
                while lp < rp and nums[lp] == nums[lp + 1]:
                    lp += 1
                while lp < rp and nums[rp] == nums[rp - 1]:
                    rp -= 1
                lp += 1
                rp -= 1
        return output