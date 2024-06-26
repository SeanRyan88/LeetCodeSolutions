# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        # Convert nodes into sorted order
        def inorder_traversal(node):
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right) if node else []
        
        # Convert list into balanced list halfing when not none
        def sorted_list_to_bst(nums):
            """Convert sorted list to balanced BST"""
            if not nums:
                return None
            mid = len(nums) // 2
            node = TreeNode(nums[mid])
            node.left = sorted_list_to_bst(nums[:mid])
            node.right = sorted_list_to_bst(nums[mid+1:])
            return node
        
        # 1. Create sorted list of node values from the BST
        sorted_values = inorder_traversal(root)
        
        # 2. Convert the sorted list to a balanced BST
        return sorted_list_to_bst(sorted_values)
        
    
