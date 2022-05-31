class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        sorted_num = sorted(nums)
        
        ans = 0
        
        for i in range(0, len(nums) - 1, 2):
            ans += sorted_num[i]
        
        return ans
