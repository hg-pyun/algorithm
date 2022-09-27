class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        ans = []
        
        for i in range(len(nums)):
            num = nums[i]
            
            find_inc = False
            find_dec = False
            
            for j in range(i, len(nums)):
                if nums[j] > num:
                    ans.append(nums[j])
                    find_inc = True
                    break;
            
            if find_inc == False:
                for k in range(0, i):
                    if nums[k] > num:
                        ans.append(nums[k])
                        find_dec = True
                        break;
            
            if find_inc == False and find_dec == False:
                ans.append(-1)
            
        return ans
