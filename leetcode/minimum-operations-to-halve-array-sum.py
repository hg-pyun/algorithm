import heapq

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        
        current_sum = sum(nums)
        target_sum = sum(nums) / 2
        heap = []
        
        for num in nums:
            heapq.heappush(heap, -1 * num)
        
        ans = 0
        
        while current_sum > target_sum:
            max_value = heapq.heappop(heap) / 2
            heapq.heappush(heap, max_value)
            current_sum += max_value
            ans += 1
        
        return ans
