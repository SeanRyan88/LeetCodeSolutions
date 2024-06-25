# Provided Class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.val = 0
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.right)
            self.val += node.val
            node.val = self.val
            dfs(node.left)
        
        dfs(root)
        return root

# Helper function to print tree in level order
def print_level_order(root):
    if not root:
        return "[]"
    result = []
    queue = [root]
    while queue:
        level = []
        next_queue = []
        for node in queue:
            if node:
                level.append(node.val)
                next_queue.append(node.left)
                next_queue.append(node.right)
            else:
                level.append(None)
        result.append(level)
        queue = next_queue
    return result

# Testing 
def build_tree_from_list(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while queue and i < len(lst):
        node = queue.pop(0)
        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    return root

# Test Cases
test_cases_bst = [
    [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8],
    [0, None, 1]
]

# Print Solution
solution_bst = Solution()
for i, lst in enumerate(test_cases_bst):
    root = build_tree_from_list(lst)
    updated_root = solution_bst.bstToGst(root)
    print(f"Test Case {i + 1}: {print_level_order(updated_root)}")