# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        def traversal(node, isLeft):
            if node.left is None and node.right is None:
                if isLeft:
                    return node.val
                else:
                    return 0
            
            left_val = traversal(node.left, True) if node.left else 0
            right_val = traversal(node.right, False) if node.right else 0
            
            return left_val + right_val
        
        return traversal(root, False)
