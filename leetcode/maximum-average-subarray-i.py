class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current = sum(nums[0:k])
        ans = current
        
        for i in range(0, len(nums) - k):
            current -= nums[i]
            current += nums[i + k]

            if current > ans:
                ans = current

        return ans / k
