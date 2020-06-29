# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        left = []
        right = []
        
        def leftTraversal(node):
            if node is None:
                left.append(None)
                return
            
            left.append(node.val)
            leftTraversal(node.left)
            leftTraversal(node.right)
        
        def rightTraversal(node):
            if node is None:
                right.append(None)
                return
            
            right.append(node.val)
            rightTraversal(node.right)
            rightTraversal(node.left)
        
        leftTraversal(root.left)
        rightTraversal(root.right)
        
        i = 0
        while i < len(left):
            if left[i] != right[i]:
                return False
            i += 1
            
        return True
        
