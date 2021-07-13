# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        
        ans = 0
        
        def traversal(node, low, high):
            if node is None:
                return;
            
            if node.val >= low and node.val <= high:
                nonlocal ans
                ans += node.val
            
            if node.val >= low:
                traversal(node.left, low, high)
            if node.val <= high:    
                traversal(node.right, low, high)
        
        traversal(root, low, high)
        
        return ans
