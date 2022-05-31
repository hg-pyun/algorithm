class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        sorted_num = sorted(nums)
        
        ans = 0
        
        for i in range(0, len(nums) - 1, 2):
            ans += min(sorted_num[i], sorted_num[i+1])
        
        return ans
