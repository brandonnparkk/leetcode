class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root: TreeNode) -> bool:
    ordered = []

    def dfs(node):
        if not node:
            return

        dfs(node.left)
        ordered.append(node.val)
        dfs(node.right)

    dfs(root)
    return all(ordered[i] < ordered[i + 1] for i in range(len(ordered) - 1))