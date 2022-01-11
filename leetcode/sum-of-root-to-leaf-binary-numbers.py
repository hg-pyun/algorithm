# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        ans = []
        
        def traversal(node, s):
            if node is None:
                return;
            
            ns = s + str(node.val)
            if node.left is None and node.right is None:
                nonlocal ans
                ans.append(ns)
                return
            
            traversal(node.left, ns)
            traversal(node.right, ns)
        
        traversal(root, '')
        
        return reduce(lambda acc, cur: acc + int(cur, 2), ans, 0)
