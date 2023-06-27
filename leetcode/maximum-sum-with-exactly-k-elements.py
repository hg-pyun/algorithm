class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        
        max_num = nums[0]

        for num in nums:
            max_num = max(max_num, num)
        
        ans = 0

        for num in range(0, k):
            ans += max_num
            max_num += 1
        
        return ans
