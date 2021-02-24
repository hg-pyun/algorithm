# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        m = [0 for _ in range(0, 100)]
        s = [0 for _ in range(0, 100)]
        
        def traversal(node, mark):
            if node is None:
                return
            
            if mark:
                m[node.val] += 1
            else:
                node.val = s[node.val]
            node.left and traversal(node.left, mark)
            node.right and traversal(node.right, mark)
            
        traversal(root, True)
        
        for i in range(len(m)):
            if m[i] > 0:
                for j in range(i, -1, -1):
                    s[j] += i
        
        traversal(root, False)
        
        return root
