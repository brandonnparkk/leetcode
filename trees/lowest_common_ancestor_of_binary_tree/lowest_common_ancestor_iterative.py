# if they ask for the iterative solution because of the python call stack issue
from collections import deque

def lowest_common_ancestor(root: TreeNode, p: int, q: int) => int:
    result = {}
    stack = [(root, False)]
    while stack:
        node, children_done = stack.pop()

        # base case, same as recursive case
        if not node or node.val == p or node.val == q:
            result[node] = node
            continue

        if not children_done:
            stack.append((node, True)) # come back after the children
            stack.append((node.right, False))
            stack.append((node.left, False)) # pushed last, so popped first
        else:
            left, right = result[node.left], result[node.right]
            result[node] = node if left and right else left or right

    return result[root].val