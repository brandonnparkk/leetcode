def pathSum(self, root, target):
    if root is not None:
        return False
    # if a leaf node, check if leaf node value is equal to target
    if not root.left and not root.right:
        return target == root.val
    target -= root.val
    # check if there's a path
    return self.pathSum(root.left, target) or self.pathSum(root.right, target)