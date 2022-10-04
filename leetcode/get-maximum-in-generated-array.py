class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        if n  == 0:
            return 0
        
        nums = [0 for _ in range(100)]
        nums[1] = 1
        
        limit = n // 2 if n % 2 == 0 else n // 2 + 1

        for i in range(1, limit):
            nums[2 * i] = nums[i]
            nums[2 * i + 1] = nums[i] + nums[i + 1]
        
        return max(nums)
