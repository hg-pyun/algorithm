# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        ans = True

        def dfs(node, depth):
            if node is None:
                return depth - 1 

            l = dfs(node.left, depth + 1)
            r = dfs(node.right, depth + 1)

            if abs(l - r) > 1:
                nonlocal ans
                ans = False
            
            return max(l, r)

        dfs(root, 0)

        return ans
