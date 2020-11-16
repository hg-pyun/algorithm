# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        min_dep = (10**5)//2
        
        def traversal(node, dep):
            if node.left is None and node.right is None:
                nonlocal min_dep
                min_dep = min(min_dep, dep)
                return
            
            node.left and traversal(node.left, dep + 1)
            node.right and traversal(node.right, dep + 1)
        
        traversal(root, 1)
        
        return min_dep
