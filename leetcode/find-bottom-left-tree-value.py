# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        
        leftmost = -1
        leftmost_depth = -1
        
        def traversal(node, depth):
            print(node.val, depth)
            nonlocal leftmost
            nonlocal leftmost_depth
            if node.left is None and depth > leftmost_depth:
                leftmost = node.val
                leftmost_depth = depth
                
            node.left is not None and traversal(node.left, depth + 1)
            node.right is not None and traversal(node.right, depth + 1)
        
        traversal(root, 0)
        
        return leftmost
