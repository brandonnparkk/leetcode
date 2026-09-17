# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        
        q = deque([root])
        depth = 1

        while q:
            level_size = len(q)
            for _ in range(level_size):
                curr = q.popleft()
                # need to skip NULL nodes
                if not curr:
                    continue
                # if it's a leaf node, we know this is the min depth
                # so just return what depth is
                if not curr.left and not curr.right:
                    return depth
                if (curr.left):
                    q.append(curr.left)
                if (curr.right):
                    q.append(curr.right)
            
            depth += 1

        return -1