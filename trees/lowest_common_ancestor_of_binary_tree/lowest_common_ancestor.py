class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root: TreeNode, p: int, q: int) -> int:
    pass
    # clarifying questions
    # is every node a different number?
        # the examples look like that's the case, but don't think that's correct
    # how small or big can the root input be?
    # can the p or q value be the same as root.val?

    # idea to implement
    # dfs, cuz we are looking as 'low' in the binary tree until we find the node.val == p or == q
    # return lowest_common_ancestor

    # implementation
    def dfs(node):
        if not node or node.val == p or node.val == q:
            return node              # base case: empty, or found a target
        left = dfs(node.left)
        right = dfs(node.right)
        if left and right:           # p and q split here
            return node
        return left or right         # pass up whichever side found something
    return dfs(root).val

    # dry_run
    # walk through your implementation
    # using: Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    # getting errors here, I believe something with the python syntax is incorrect.