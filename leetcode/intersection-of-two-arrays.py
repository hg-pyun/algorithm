class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans = []
        checker = {}
        
        for num in set(nums1):
            checker[num] = True
        
        for num in set(nums2):
            if num in checker:
                ans.append(num)
        
        return ans
