def right_side_view(root: TreeNode) -> list[int]:
    res = []

    def dfs(node, depth):
        if not node:
            return
        # first node we reach at this depth is the rightmost one
        if depth == len(res):
            res.append(node.val)
        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)   # still explore left for deeper levels

    dfs(root, 0)
    return res