# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        map = {}

        def dfs(node, map):
            if node is None:
                return False
                
            if (k - node.val) in map:
                return True
            else:
                map[node.val] = True

            return dfs(node.left, map) or dfs(node.right, map)
        
        return dfs(root, map)
