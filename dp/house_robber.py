# recursion
# O(2^n) - calls the same inputs multiple times
def rob(treasure):
    if not treasure:
        return 0

    def rob_helper(i):
        if i == 0:
            return 0
        if i == 1:
            return treasure[0]

        skip = treasure[i - 1]
        take = treasure[i - 2] + treasure[i - 1]
        return max (skip, take)
    return rob_helper(len(treasure))

# memoization (top-down)
# o(n) - goes through list exactly once
def rob(treasure):
    if not treasure:
        return 0

    # initialize memoization dictionary
    memo = {}

    def rob_helper(i):
        # base cases
        if i == 0:
            return 0
        if i == 1:
            return treasure[0]

        # check and return value from memo BEFORE making any recursive calls
        if i in memo:
            return memo[i]

        # recursive relation
        skip = rob_helper(i - 1)
        take = rob_helper(i - 2) + treasure[i - 1]
        memo[i] = max(skip, take)
        return memo[i]
    return rob_helper(len(treasure))

# Bottom-Up Approach
# O(n) - goes through each optimal solution once just like memoization
def rob(treasure):
    if not treasure:
        return 0

    # init dp array, need to add 1 because we are passing the 0 case
    dp = [0] * len(treasure) + 1
    # fill in the base cases
    dp[1] = treasure[0]
    # iterate through the rest of the list
    for i in range(2, len(treasure) + 1):
        # fill in dp[i] using recurrence relation
        skip = dp[i - 1]
        take = dp[i - 2] + treasure[i - 1]
        dp[i] = max(skip, take)

    # returns the value of the last item in dp
    return dp[len(treasure)]

# Further optimization
# you can see you only need the 2 MOST RECENT values to calc the next value.
# this reduces the space complexity from O(n) to O(1).
def rob(treasure):
    if not treasure:
        return 0

    curr, prev = 0, treasure[0]
    for i in range(2, len(treasure) + 1):
        # calc the next value of dp
        skip = curr
        take = prev + treasure[i - 1]
        prev, curr = curr, max(skip, take)
    return curr
