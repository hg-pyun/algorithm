# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        
        if d == 1:
            return TreeNode(v, root)
            
        
        def traversal(node, depth, prev, direct):
            if depth == d:
                new = TreeNode(v)
                
                if direct == 'left':
                    new.left = node
                    prev.left = new
                elif direct == 'right':
                    new.right = node
                    prev.right = new
        
            if node is None:
                return
            
                
            traversal(node.left, depth + 1, node, 'left')
            traversal(node.right, depth + 1, node, 'right')
        
        traversal(root, 1, None, None)
        return root
