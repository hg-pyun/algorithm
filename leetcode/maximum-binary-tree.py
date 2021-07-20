# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        
        max_index = -1
        max_value = -1
        for i in range(len(nums)):
            if max_value < nums[i]:
                max_index = i
                max_value = nums[i]
        
        left_nums = nums[0:max_index]
        right_nums = nums[max_index+1:]
        
        left_node = self.constructMaximumBinaryTree(left_nums)
        right_node = self.constructMaximumBinaryTree(right_nums)
        
        return TreeNode(max_value, left_node, right_node)
