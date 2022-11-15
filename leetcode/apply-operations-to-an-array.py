class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        for _ in range(len(nums) - 1):
            for j in range(len(nums) - 1):
                if nums[j] == 0:
                    nums[j] = nums[j + 1]
                    nums[j + 1] = 0
        
        return nums
