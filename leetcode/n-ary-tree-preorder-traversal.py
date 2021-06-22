"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        ans = []
        
        def traversal(node):
            if node is None:
                return;
            
            ans.append(node.val)
            
            for n in node.children:
                traversal(n)
        
        traversal(root)
        
        return ans
        
