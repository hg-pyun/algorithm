# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_sum = -math.inf
    
    def maxPathSum(self, root: TreeNode) -> int:
        self.traversal(root)
        return self.max_sum
    
    def traversal(self, node):
        left = self.traversal(node.left) if node.left is not None else 0
        right = self.traversal(node.right) if node.right is not None else 0
        
        cur_sum = max(node.val, node.val + left, node.val + right)
        self.max_sum = max(self.max_sum, cur_sum, node.val + left + right)
        return cur_sum
