# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        levels = {}
        
        def traversal(node, dep):
            if node is None:
                return
            
            if dep in levels:
                levels[dep].append(node.val)
            else:
                levels[dep] = [node.val]
            
            traversal(node.left, dep + 1)
            traversal(node.right, dep + 1)
            
        traversal(root, 1)
        
        ans = []
        
        for key in levels:
            candidates = sorted(levels[key], reverse=True)
            ans.append(candidates[0])
        
        return ans
