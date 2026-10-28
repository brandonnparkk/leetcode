class Solution:
    def rob(self, nums: List[int]) -> int:
        # ask clarifying questions
        # will each num always be > 0? no can also be 0
        # will len of nums be > 0? no
        # if len of nums is 1, then return value?
        
        # framing this by simplifying the question
        # let's say i only have [1,3,5]
        # max will be 3 or 1 + 5
        
        # dfs because:
        # 1. choice depends on answers to smaller versions of same question
        # 2. you have to make a choice: will you rob the last house? or skip and rob 2nd to last?
        # dfs(i) = max money from robbing the first i house
        def dfs(i):
            # identify the base case
            # 1. return value if len(nums) == 1
            # 2. return 0 if len(nums) 0

            if i == 0:
                return 0
            
            if i == 1:
                return nums[0]

            skip = dfs(i - 1)
            take = dfs(i - 2) + nums[i - 1]
            max_money = max(skip, take)
            return max_money
        
        return dfs(len(nums))
    
        # remember to dry run
        # walk through the solution to make sure it works

        # time and space complexity
        # time complexity: O(2^n), because the tree is n levels deep and each level can at most double the level above it. because the node has a left and right. (1 -> 2 -> 4 -> 8...)
            # - we call the same dfs(i) multiple times even thought we already know it's result.
        # space complexity: O(n)
            # - is the height of the recursion tree, because we only go as far deep on one path from root to a leaf.

        