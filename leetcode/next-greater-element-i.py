class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        index_map = {}
        
        for i in range(len(nums2)):
            index_map[nums2[i]] = i
            
        ans = []
        
        for n in nums1:
            target_index = index_map[n]
            
            if target_index == len(nums2) - 1:
                ans.append(-1)
            else:
                find = False
                for j in range(target_index, len(nums2)):
                    if nums2[j] > n:
                        ans.append(nums2[j])
                        find = True
                        break;
                        
                find == False and ans.append(-1)
        
        return ans
