class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root: TreeNode) -> bool:
    # Write your solution here
    pass
    # clarifying questions
    # how small or big can root be?
    # how small or big can the actual items in root be?
    # is a valid binary search tree always have root node, and 1 left and 1 right or
    # can it be just root? if that's the case, do we output true or false?

    # idea for implementation
    # because traversing down as far as we can and checking if left < root, and right > root
    # thinking of using a dfs approach
    
    # go through all the values in root
        # if len <= 3:
            # return false
        # use dfs to check the node.left side < node.val
        # use dfs to check the node.right side > node.val
        # if both conditions are met, return true
        # else return false

    # implementation
    is_valid = true
    
    def dfs(node):
        if not node:
            return
        
        # post-order traversal
        # implement recursive dfs function
        # then, check for condition met; do something
        left = dfs(node.left)
        right = dfs(node.right)

        if left_n.val > node.val or right_n.val < node.val:
            is_valid = false

    dfs(root)
    return is_valid

    # dry_run
    # root = [5,1,4,null,null,3,6]

    # dry run works

    # submit
