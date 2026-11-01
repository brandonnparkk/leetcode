class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: TreeNode) -> TreeNode:
    """Invert the binary tree rooted at root and return the root."""
    pass

    # space complexity: O(v + e) could be O(1)
    # dfs

    # clarifying questions
    # if input tree is empty, what happens?
        # return []
    # how many nodes are there potentially?
        # in between 0 and 100.
        # green light to use recursive dfs
    
    # idea to implement
    # preorder: swap first then recurse
    # inorder: left, node, right, it's not a binary search tree - balanced.
    # postorder: recurse first, then swap

    # 2
    # 1 3

    # 2
    # 3 1
    
    # loop through the nodes in input
    # dfs helper - node
        # base case if empty tree
        # swap left and right
        # recurse
    # run dfs
    # return input

    # implementation
    def dfs(node):
        if not node:
            return
        # swap left and right
        # if we are going with idea for implementation,
        # then, the calculation should be done here.
        node.left, node.right = node.right, node.left
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return root

    # dry run
    # based on experiment, it seems like problem uses postorder traversal
