class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sorted_nums = sorted(set(nums), reverse=True);
        return sorted_nums[2] if len(sorted_nums) > 2 else sorted_nums[0]
