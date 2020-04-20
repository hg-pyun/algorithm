# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def makeTree(self, val, node):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
                return
            else:
                self.makeTree(val, node.left)
        else:
            if node.right is None:
                node.right = TreeNode(val)
                return
            else:
                self.makeTree(val, node.right)
            
    
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        
        for i in range(1, len(preorder)):
            self.makeTree(preorder[i], root)
        
        return root
