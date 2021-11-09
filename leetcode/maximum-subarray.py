class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ans = nums[0]
        sub_sum = 0
        
        for num in nums:
            sub_sum += num
            ans = max(sub_sum, ans)
            
            if sub_sum < 0:
                sub_sum = 0
        
        return ans
        
