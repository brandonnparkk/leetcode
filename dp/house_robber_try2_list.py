class Solution:
    def rob(self, nums: List[int]) -> int:
        # create the array with what we know
        # aka the base cases
        dp = ([0] * len(nums) + 1)
        dp[1] = nums[0]

        # iterate through the rest of the list
        for i in range(2, len(nums) + 1):
            # fill in the dp[i] using recurrence
            skip = dp[i - 1]
            take = dp[i - 2] + nums[i - 1]
            dp[i] = max(skip, take)
        
        return dp[len(nums)]

        # time and space complexity
        # time complexity: O(n), The loop runs n − 1 times, and each iteration does O(1) work: two lookups, an addition, a max, and an assignment.
        # space complexity: O(n)
            # - The dp array stores n + 1 integers. No recursion, so there’s no call stack cost.
        # Bottom up approach: you start with dp[0] → dp[1] → ... → dp[n], not dfs(...).
        