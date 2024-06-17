# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        next = targetSum - root.val

        if root.left is None and root.right is None:
            return next == 0

        left = self.hasPathSum(root.left, next)
        right = self.hasPathSum(root.right, next)

        return left or right
