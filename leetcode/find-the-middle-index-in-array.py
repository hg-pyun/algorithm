class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        left = 0
        right = 0
        
        for num in nums:
            right += num;
            
        ans = -1
        
        for i in range(len(nums)):
            right -= nums[i]

            if left == right:
                ans = i
                break
            
            left += nums[i]
        
        return ans
