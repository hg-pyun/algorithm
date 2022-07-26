class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    
        l = 0
        r = len(nums) - 1
        index = -1
        ans = [-1, -1] 
        
        if len(nums) == 0:
            return ans
        
        while (l <= r):
            mid = (l + r) // 2
            
            if nums[mid] == target:
                index = mid
                break;
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        if index == -1:
            return ans
        
        for i in range(index, -1, -1):                
            if nums[i] != target:
                break;
            else:
                ans[0] = i
            
        for i in range(index, len(nums)):
            if nums[i] != target:
                break;
            else:
                ans[1] = i
                
        return ans
