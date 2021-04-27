# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        
        candidate = []
        
        def traversal(node, candidate):
            if node is None:
                return
            
            traversal(node.left, candidate)
            candidate.append(node.val)
            traversal(node.right, candidate)
        
        traversal(root, candidate)
        
        check = {}
        ans = []
        maximum = -1
        hasMode = False
        
        for v in candidate:
            if v in check:
                hasMode = True
                check[v] += 1
                maximum = max(maximum, check[v])
            else:
                check[v] = 1
        
        for v in candidate:
            if check[v] == maximum:
                ans.append(v)
                
        return set(ans) if hasMode else check
