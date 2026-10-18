# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# ** when the problems involves "root-to-leaf" paths, you should use helper function as necessary.
# this allows to introduce extra params that store the state of our current path.

# solution: global variables are preferred when we need to collect values in a list
# as we traverse the binary tree.

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # If I'm a node in the tree,
        # I need to calculate the number of good nodes in my left subtree
        # and number of good nodes in my right subtree.

        # then, if I know the two values, I can return the num of good nodes by adding them together
        # add adding 1 if the current node is a good node.

        # Base Case: The number of good nodes in an empty tree is 0.
        # How to determine if node is "good": need max val of any node on the path starting from the root to the current node.
        # need a helper func that introduces "max_", which represents the max value seen so far.
        # to check if the current node is a good node, we compare current node's value to max_. if current node is greater than or equal to max_, then current node is good.

        #***Tricks:
        # 1. a node is good depends on the running max along the path, not if parent is good.
        # 2. a path like 3 -> 1 -> 3, if still good because our check is "greater than or equal to".
        def dfs(root, max_):
            # base case
            if root is None:
                return 0

            count = 0
            if root.val >= max_:
                # good node found, update count and max_
                count += 1
                max_ = root.val

            # recurse and pass down updated max_
            # to the left and right children
            left = dfs(root.left, max_)
            right = dfs(root.right, max_)

            # return the num of good nodes in the subtree
            # rooted at the current node
            return count + left + right

        return dfs(root, -float("inf"))

