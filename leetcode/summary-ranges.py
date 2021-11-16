class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        ans = []
        
        current_range = ""
        count = 0
        
        for i in range(len(nums)):
            if current_range == "":
                current_range += str(nums[i])                    
            
            if i+1 == len(nums) or nums[i+1] - nums[i] > 1:
                if count > 0:
                    current_range += "->"
                    current_range += str(nums[i])
                
                ans.append(current_range)
                current_range = ""
                count = 0
            else:
                count += 1
            
        return ans
