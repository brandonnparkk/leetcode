# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        
        result = []
        queue = deque([root])

        while queue:
            # number of nodes at the current level
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                curr = queue.popleft()
                current_level.append(curr.val)
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            # the current level is finished
            # its last element is the rightmost one
            result.append(curr.val)
            
        return result     