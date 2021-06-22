# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        
        ans = []
        count = {}
        
        def traversal(node):
            if node is None:
                return 0
            
            left_val = traversal(node.left)
            right_val = traversal(node.right)
            
            sum_val = left_val + right_val + node.val
            
            if sum_val in count:
                count[sum_val] += 1
            else:
                count[sum_val] = 1
            
            return sum_val
        
        traversal(root)

        most_freq = -1
        for key in count:
            most_freq = max(count[key], most_freq)
            
        for key in count:
            if count[key] == most_freq:
                ans.append(key)
                
        return ans
        
