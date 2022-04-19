class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            left = abs(nums[l])
            right = abs(nums[r])
            
            if left > right:
                ans[r - l] = left * left
                l += 1
            else:
                ans[r - l] = right * right
                r -= 1
        
        return ans
        
