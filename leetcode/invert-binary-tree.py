# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        def traversal(node):
            if node is None:
                return
            
            temp = node.left
            node.left = node.right
            node.right = temp
            
            traversal(node.left)
            traversal(node.right)
        
        traversal(root)
        return root
