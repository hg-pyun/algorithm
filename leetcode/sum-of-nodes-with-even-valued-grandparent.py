# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = []
        
        def traversal(node):
            if node is None:
                return
            
            if node.val % 2 == 0:
                traversal_edge_node(node, 0)
            
            traversal(node.left)
            traversal(node.right)
        
        def traversal_edge_node(node, step):
            if node is None: 
                return
            
            if step == 2:
                ans.append(node.val)
                return
            
            traversal_edge_node(node.left, step + 1)
            traversal_edge_node(node.right, step + 1)
            
        traversal(root)
        return reduce(lambda a, b: a + b, ans, 0) if ans else 0
