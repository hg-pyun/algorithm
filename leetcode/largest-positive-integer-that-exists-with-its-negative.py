class Solution:
    def findMaxK(self, nums: List[int]) -> int:

        positive_nums = []
        map = {}

        for num in nums:
            if num < 0 and abs(num) not in map:
                map[abs(num)] = 1
            
            if(num > 0):
                positive_nums.append(num)

        for num in sorted(positive_nums, reverse=True):
            if num in map:
                return num

        return -1
