# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        queue = [root]
        ans = []
        
        while (queue):
            divide = len(queue)
            count = len(queue)
            s = 0
        
            while (count > 0):
                node = queue.pop(0)
                count -= 1
                s += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ans.append(s/divide)
    
        return ans
