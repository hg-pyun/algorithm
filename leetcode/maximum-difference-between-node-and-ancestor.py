# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        ans = -1
        
        def traversal(node, anc):
            if node is None:
                return    
        
            for item in anc:
                nonlocal ans
                ans = max(ans, abs(item - node.val))
            
            anc.append(node.val)
            
            node.left and traversal(node.left, copy.deepcopy(anc))
            node.right and traversal(node.right, copy.deepcopy(anc))
        
        
        traversal(root, [root.val])
        
        return ans
