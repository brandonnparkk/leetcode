class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameter_of_binary_tree(root: TreeNode) -> int:
    pass
    # 1. try to solve ourselves
    # 2. copy and paste what I have so far, into claude
    # and ask claude what are the gaps I have and how I can get to the solution

    # clarifying questions
    # 1. can root be empty?
    #     yes
    # 2. will the nodes always be increasing?
    #     can be
    # 3. (ask claude) can you help me understand what diameter means in this context.

    # idea for implementation
    # create a output var
    # if empty, return 0
    # loop through the root
    # use dfs - why? because of longest path
    # recursive dfs
    # when run DFS, then increment output
    # at the end, return output

    # implementation
    output = 0
    
    def dfs(node):
        nonlocal output
        if not node:
            return 0
        # need something here to handle nodes with left and right value
        left = dfs(node.left)
        right = dfs(node.right)
        output = max(output, left + right)
        return 1 + max(left, right)
        

    dfs(root)
    return output
    # dry_run

    # submit

    # postorder DFS
    # preorder DFS
    # inorder DFS
    # - figure out the differences for each and when to use them