class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)
        
        while lo < hi:
            mid = math.floor((lo + hi)/2)
            
            if str(nums[mid] < nums[0]) == str(target < nums[0]):
                num = nums[mid]
            else:
                num = -math.inf if target < nums[0] else math.inf
                    
            if num < target:
                lo = mid + 1
            elif num > target:
                hi = mid
            else:
                return mid
            
        return -1
