class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i == 0:
                return 0
            if i == 1:
                return nums[0]

            if i in memo:
                return memo[i]

            skip = dfs(i - 1)
            take = dfs(i - 2) + nums[i - 1]
            max_money = max(skip, take)
            memo[i] = max_money
            return memo[i]
        
        return dfs(len(nums))

        # time and space complexity
        # time complexity: O(n), because we only call each value once and check the memo if it exists, just use that value
        # space complexity: O(n)
            # - is the height of the recursion tree, because we only go as far deep on one path from root to a leaf.

        # Top down approach: you start with dfs(5) -> dfs(4) -> ... -> dfs(1)
        