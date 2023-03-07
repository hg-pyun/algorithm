class Solution:
    def minOperations(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        op = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                diff = nums[i - 1] - nums[i] + 1
                op += diff
                nums[i] = nums[i] + diff
        
        return op
