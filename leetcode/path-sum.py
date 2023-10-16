# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        def dfs(node, s, targetSum):
            if node is None:
                return

            current_target = s + node.val

            # leaf
            if node.left is None and node.right is None:
                return current_target == targetSum

            left = dfs(node.left, current_target, targetSum)
            right = dfs(node.right, current_target, targetSum)

            return left or right
            
        
        return dfs(root, 0, targetSum)
        
