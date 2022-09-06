"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if root is None:
            return []
        
        queue = [root]
        ans = []
        
        while (queue):
            local_ans = [];
            count = len(queue)
        
            while (count > 0):
                node = queue.pop(0)
                count -= 1
                local_ans.append(node.val)
                
                for child in node.children:
                    queue.append(child)
            
            ans.append(local_ans)
    
        return ans
