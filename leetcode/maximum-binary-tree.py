# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findIndex(self, nums):
        max_num = nums[0]
        target_index = 0
        for i in range(len(nums)):
            if max_num < nums[i]:
                target_index = i
                max_num = nums[i]
        
        return target_index

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        if len(nums) == 1:
            return TreeNode(nums[0])

        largest_num_index = self.findIndex(nums)
        
        left = self.constructMaximumBinaryTree(nums[:largest_num_index])
        right = self.constructMaximumBinaryTree(nums[largest_num_index+1:])

        return TreeNode(nums[largest_num_index], left, right)
