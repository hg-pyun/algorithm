# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        result = 0
        count = 0
        def inorder(node):
            node.left is not None and inorder(node.left)
            nonlocal count
            nonlocal result
            count += 1
            if count == k:
                result = node.val
                return
            node.right is not None and inorder(node.right)
        
        inorder(root)
        return result
