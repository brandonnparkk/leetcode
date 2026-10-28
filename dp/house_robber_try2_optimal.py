class Solution:
    def rob(self, nums: List[int]) -> int:
        # create the array with what we know
        # aka the base cases
        curr, prev = 0, nums[0]

        # iterate through the rest of the list
        for i in range(2, len(nums) + 1):
            # calculate the next value of dp
            skip = curr
            take = prev + nums[i - 1]
            # slide the window forward
            prev, curr = curr, max(skip, take)

        return curr
        
        # time and space complexity
        # time complexity: O(n), The loop runs n − 1 times, and each iteration does O(1) work: two lookups, an addition, a max, and an assignment.
        # space complexity: O(1)
            # - The count doesn’t grow with n, so it’s constant space. fixed number of variables, so they’re O(1).
        