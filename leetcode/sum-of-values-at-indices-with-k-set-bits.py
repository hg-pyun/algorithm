class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0

        for i in range(len(nums)):
            if self.count_bits(i) == k:
                ans += nums[i]
            
        return ans

    def count_bits(self, num: int) -> int:
        return bin(num).count('1')
