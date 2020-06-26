# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        result = 0
        
        def traversal(node, s):
            if node.left is None and node.right is None:
                nonlocal result
                result += int(s + str(node.val))
                return
            
            node.left is not None and traversal(node.left, s + str(node.val))
            node.right is not None and traversal(node.right, s + str(node.val))
            
        traversal(root, '')
            
        return result
