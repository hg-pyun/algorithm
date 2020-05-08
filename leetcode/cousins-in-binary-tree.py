# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.x_dep = None
        self.x_p_val = None
        self.y_dep = None
        self.y_p_val = None
    
    def traversal(self, node, p_val, x, y, dep):
        if node is None:
            return
        
        if node.val == x:
            self.x_dep = dep
            self.x_p_val = p_val
        elif node.val == y:
            self.y_dep = dep
            self.y_p_val = p_val
        
        self.traversal(node.left, node.val, x, y, dep + 1)
        self.traversal(node.right, node.val, x, y, dep + 1) 
    
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.traversal(root, None, x, y, 0)
        
        return self.x_dep == self.y_dep and self.x_p_val != self.y_p_val
