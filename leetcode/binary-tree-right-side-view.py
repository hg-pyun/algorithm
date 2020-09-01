# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        output = []
        
        if not root:
            return output
        
        m = {}
        
        def traversal(node, dep):     
            if dep in m:
                m[dep].append(node.val)
            else:
                m[dep] = [node.val]
            
            node.left and traversal(node.left, dep + 1)
            node.right and traversal(node.right, dep + 1)
            
        traversal(root, 0)
        
        for dep in m:
            output.append(m[dep].pop())
            
        return output
