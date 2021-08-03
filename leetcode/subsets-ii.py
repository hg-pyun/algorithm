class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        
        for i in range(1 << n):
            subset = []
            for j in range(n):
                if i & (1 << j):
                    subset.append(nums[j])
                    
            is_diff = True
            subset.sort()
            for arr in result:
                arr.sort();
                if arr == subset:
                    is_diff = False
                    break
                    
            if is_diff:
                result.append(subset)
        
        return result
