# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        ans = True
        
        def traversal(node_p, node_q):
            nonlocal ans
            if node_p is None and node_q is None:
                return
            if node_p is None or node_q is None:
                ans = False 
                return
            
            if node_p.val != node_q.val:
                ans = False
                return
            
            traversal(node_p.left, node_q.left)
            traversal(node_p.right, node_q.right)
        
        traversal(p, q)
        
        return ans
