# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:        
        
        nums = []
        
        def traversal(node):
            if node is None:
                return;
            
            left = node.left and traversal(node.left)
            nums.append(node.val)
            right = node.right and traversal(node.right)
            
        traversal(root)
        ans = 999
        
        
        for i in range(len(nums) - 1):
            diff = nums[i + 1] - nums[i]
            ans = min(ans, nums[i + 1] - nums[i])
            
        return ans
