# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.length = 0
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.traversal(root)
        return self.length
        
    def traversal(self, node):
        left = node.left is not None and self.traversal(node.left) + 1
        right = node.right is not None and self.traversal(node.right) + 1
        
        self.length = max(self.length, left + right)
        return max(left, right)
        
