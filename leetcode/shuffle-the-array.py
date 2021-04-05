class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        
        for i in range(0, len(nums) // 2):
            ans.append(nums[i])
            ans.append(nums[i+n])
            
        return ans
