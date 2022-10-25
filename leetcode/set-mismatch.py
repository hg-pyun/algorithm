class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        checker = [0 for i in range(len(nums) + 1)]
        
        for num in nums:
            checker[num] += 1
            
        dup = 0
        mismatch = 0
        
        for i in range(len(checker)):
            if i == 0:
                continue
            
            if checker[i] == 2:
                dup = i
            if checker[i] == 0:
                mismatch = i
        
        return [dup, mismatch]
