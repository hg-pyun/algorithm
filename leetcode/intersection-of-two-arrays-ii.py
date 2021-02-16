class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = {}
        count2 = {}
        
        for n in nums1:
            if n in count1:
                count1[n] += 1
            else:
                count1[n] = 1
        
        for n in nums2:
            if n in count2:
                count2[n] += 1
            else:
                count2[n] = 1
        
        ans = []
        
        for k in count2:
            if k in count1:
                while (count1[k] and count2[k]):
                    ans.append(k)
                    count1[k] -= 1
                    count2[k] -= 1
        
        return ans
