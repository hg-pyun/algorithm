"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if root is None:
            return root
        
        queue = [root]
        row = []
        
        while (queue):
            
            while(queue):
                row.append(queue.pop(0))
            
            for i in range(len(row) - 1):
                row[i].next = row[i + 1]
                
            for node in row:
                node.left and queue.append(node.left)
                node.right and queue.append(node.right)
            
            row = []
        
        return root
