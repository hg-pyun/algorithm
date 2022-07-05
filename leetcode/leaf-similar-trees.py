# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        left = []
        right = []
        
        def pre_order(node, seq):
            
            if node is None:
                return;
            
            if node.left is None and node.right is None:
                seq.append(node.val)
    
            node.left and pre_order(node.left, seq)
            node.right and pre_order(node.right, seq)
        
        pre_order(root1, left)
        pre_order(root2, right)
        
        if len(left) != len(right):
            return False
        
        for i in range(len(left)):
            if left[i] != right[i]:
                return False
        
        return True
