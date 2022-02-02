class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        m = {}
        
        for i in range(len(nums)):
            num = nums[i]
            expected = target - num
            
            if num in m:
                return [m[num], i]
            else:
                m[expected] = i
