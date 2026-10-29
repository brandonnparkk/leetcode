# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            # set up base case
            if not node:
                return 0
            # set count
            count = 1 if node.val >= max_so_far else 0
            # set up new max
            new_max = max(node.val, max_so_far)
            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)
            return count

        return dfs(root, root.val)