# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # 0 False
    # 1 True
    # 2 OR
    # 3 AND
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
                
        left = root.left and self.evaluateTree(root.left)
        right = root.right and self.evaluateTree(root.right)
        
        if left is None and right is None:
            return root.val
        
        if root.val == 2:
            return left or right
        else:
            return left and right
